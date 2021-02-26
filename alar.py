
from pygame import mixer
import time
import pygame,sys
from pygame.locals import *



def alarmaE():
    mixer.init()
    sound = mixer.Sound('alarma1.wav')
    sound.play()
        

def alarmaStop():
    mixer.init()
    sound = mixer.Sound('alarma1.wav')
    sound.stop()