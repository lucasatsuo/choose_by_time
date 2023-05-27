# Created by Lucas Atsuo Ito
# For a Perfect Pinball project
# May of 2023

from time import time
from msvcrt import kbhit
from os import system
from configparser import ConfigParser

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

if __name__=='__main__':
    config = readConfiguration()

    print("PRESS any button to start Jukebox!!")
    start = time()
    has_keyed = False
    curr_time = 0
    while(time()-start < int(config['pinball']['SecondsWaiting'])):
        if kbhit():
            has_keyed = True
            break
        if time()-start > curr_time:
            print(f"starting pinball in {curr_time} seconds..")
            curr_time += 1

    if has_keyed:
        print('Interrupted!!')
        system(f"{config['jukebox']['FileName']}")
    else:
        system(f"{config['pinball']['FileName']}")
