from pygame import mixer
from datetime import datetime
from time import time
def dwater(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == 'stop':
            mixer.music.stop()
            break
def log_now(msg):
    with open("log.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':

    init_water= time()
    init_watertime=5
    while True:
        if time() - init_water> init_watertime:
            print("It's Time To Drink Water. Enter 'Drank' to stop")
            dwater("song.mp3", "stop")
            init_water=time()
            log_now("Drank water at ")
