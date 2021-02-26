# face
1. Crear un entorno en anconda
2. Instalar las librerias con el comando:
    - pip install -r requirements.txt

Nota: puede que las librerias  den error, esto puede ocurrir si usas una version
de python diferente, este proyecto se usa:
- Python 3.7.9
- pip 21.0.1 
3. Para ejecutar el analisis traves de webcam
    python menu.py
    El menu que se ejecuta tendra 3 opciones:
    - 1. Habre la webcam y comienza analizar
        Nota: lo puntos de refencia estan asignados segun el espacio y perspectiva del
        lugar donde esty haciendo la ejecucion, para poder entender este putno primero ejecute laprueba con video locales
    - 2. La segunda opcion sirve para subir los videogenerados a tu drive
        Nota: para ejecutar este servicio se debe crear una app en google cloud y habilitar la pai de
        drive. Revise la siguiente documentacion en google cloud.
        Ademas se debe configurar los servicios de ID de clientes OAuth 2.0
        Esto sirve para gregar a losusuarios que pueden consumir la api.
        Y  debe decargar un archivo en formtato en json con las credenciales generadas, y ponerle de nombre client_secrets y ubicarlo en la direccion actual.
    - 3. Se realiza pruebas de la funcion alarma
    - 4. Sale del programa 

4. Para ejecutar el analisis para video locales
el video debe estar en la carpeta actual 
    python maLocal.py --videopath "nombre.extension"
    ejemplo 
    python maLocal.py --videopath "video.mp4"

- Funcionamiento de los puntos:
Los primeros 4 de los 6 puntos requeridos se utilizan para marcar la región de interés (ROI) donde desea monitorear. Además, las líneas marcadas por estos puntos deben ser líneas paralelas en el mundo real como se ve desde arriba. Por ejemplo, estas líneas podrían ser los bordillos de la carretera.
Estos 4 puntos deben proporcionarse en el orden predefinido que sigue.

--Primeros 4 puntos:
   - 1. Punto 1: abajo-izquierda 
   - 2. Punto 2: abajo-derecha
   - 3. Punto 3: arriba-izquierda 
   - 4. Punto 4: arriba-derecha

--Ultimos 2 puntos 
Los ultimos 2 puntos son usados  como marcas,2  puntos separados  a un 1.80 metros en la región de interés. Por ejemplo, esta podría ser la altura de una persona (más fácil de marcar en el marco).

 5. Para ejecutar analisis en una camra ip
    debes instalar la app en un dispositivo android: 
    url app:https://play.google.com/store/apps/details?id=com.pas.webcam&hl=es_EC&gl=US
    cuando incies el servidor de la camara ip en tu celular
    te parece una url asi: http://192.168.1.102:8080
    Puedes comprobar video con la aplicacion vcl, con la opcion de reproduccion en red
    Pero para poder reproducir se debere agregar  /video: http://192.168.1.102:8080/video
   
    Nota: si se le pone usuario y contraseña al servidor de la cmara ip, no se podra conectar 
    para realizar el analsis

