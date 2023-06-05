# Created by Lucas Atsuo Ito
# For a Perfect Pinball project
# May of 2023

import pygame
from sys import exit
from time import time
from os import system
from configparser import ConfigParser

pygame.init()

JUKEBOX_ART = r"""
Starting JUKEBOX
   _       _        _               
  (_)     | |      | |              
   _ _   _| | _____| |__   _____  __
  | | | | | |/ / _ \ '_ \ / _ \ \/ /
  | | |_| |   <  __/ |_) | (_) >  < 
  | |\__,_|_|\_\___|_.__/ \___/_/\_\
 _/ |                               
|__/                                  
"""

PINBALL_ART = r"""
Starting the PINBALL game
       _       _           _ _ 
      (_)     | |         | | |
 _ __  _ _ __ | |__   __ _| | |
| '_ \| | '_ \| '_ \ / _` | | |
| |_) | | | | | |_) | (_| | | |
| .__/|_|_| |_|_.__/ \__,_|_|_|
| |                            
|_|  
"""




def readConfiguration():
# Read from file configuration.ini 
    Config = ConfigParser()
    fileRead = Config.read("configuration.ini")
    if fileRead == []:
        print("Make sure the file 'configuration.ini' is set")
        exit(1)
    
    config_dict = {
        'pinball':{
            'FileName':Config.get('pinball','FileName'),
            'GameTitle':Config.get('pinball','GameTitle'),
            'SecondsWaiting':Config.get('pinball','SecondsWaiting'),
            'SelectButton':Config.get('pinball','SelectButton'),
            'SelectButtonName':Config.get('pinball','SelectButtonName')},
        'jukebox':{
            'FileName':Config.get('jukebox','FileName'),
            'GameTitle':Config.get('jukebox','GameTitle'),
            'SelectButton':Config.get('jukebox','SelectButton'),
            'SelectButtonName':Config.get('jukebox','SelectButtonName')}
        }
    
    return config_dict

def coisa():
    pygame.display.init()
    verdade=True
    print('comeco')
    while(verdade):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                verdade = False
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
            jj = joysticks[0]


if __name__=='__main__':
    config = readConfiguration()

    print("PRESS any button to start Jukebox!!")
    start = time()
    has_keyed = False
    curr_time = 0

    pygame.display.init()
    while(time()-start < int(config['pinball']['SecondsWaiting'])):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                has_keyed = True
            # whithout following line, wont work!!
            joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())] # this is needed to listen for controller events
        if has_keyed: break
        if time()-start > curr_time:
            print(f"starting pinball in {int(config['pinball']['SecondsWaiting'])-curr_time} seconds..")
            curr_time += 1

    if has_keyed:
        print(JUKEBOX_ART)
        system(f"{config['jukebox']['FileName']}")
    else:
        print(PINBALL_ART)
        system(f"{config['pinball']['FileName']}")

