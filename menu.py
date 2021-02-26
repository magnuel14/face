from main import *
from quickstart import *
from alarma import *


def pedirNumeroEntero():
     
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Reconocimiento de distancia social")
    print ("2. Subir el video")
    print ("3. Opcion 3")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Solo se procesa los fotogramas en que se detecte una persona ")
        face()

    elif opcion == 2:
        print ("Autentiquese para guardar el archivo")
        gurdarArchivo()
    elif opcion == 3:
        print("Opcion 3")
        alarma()
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
    