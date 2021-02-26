
from pygame import mixer
import time
import pygame,sys
from pygame.locals import *
from alar import *

def alarma():
    mixer.init()
    sound = mixer.Sound('alarm.wav')


    def pedirNumeroEntero():
        
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Menu audio: "))
                correcto=True
            except ValueError:
                print('Error, introduce un numero entero')
        
        return num
    
    salir = False
    opcion = 0
    
    while not salir:
    
        print ("1. Alarma")
        print ("2. Salir 2")
        print ("3. Salir 3")        
        print ("Elige una opcion")
    
        opcion = pedirNumeroEntero()
    
        if opcion == 1:
            print ("Opcion 1")
            alarmaE()
        elif opcion == 2:
            print ("Opcion 2")
            alarmaStop()
        
        
        elif opcion == 3:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 3")
    
    print ("Fin")
        