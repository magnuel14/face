import cv2
import os
import argparse
from network_model import model
from aux_functions import *
#controlar video
import argparse
import imutils

def face():
    # Suprime abvertencias de TensorFlow 
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    #variable que guarda los puntos
    mouse_pts = [(0, 477), (636, 479), (3, 3), (636, 8), (2, 362), (614, 376), (456, 301)]
    count =1
    #funcion para encontrar los puntos
    '''
    def get_mouse_points(event, x, y, flags, param):
        # Se usa para marcar 4 puntos en el cuadro cero del video que se deformarán
        # Se usa para marcar 2 puntos en el cuadro cero del video que están a 180 centrimetros de distancia
        global mouseX, mouseY, mouse_pts
        # si das click creas un evento
        if event == cv2.EVENT_LBUTTONDOWN:
            #se captura la cordenada del click en x y en y
            mouseX, mouseY = x, y
            #dibuja un circulo amarillo
            cv2.circle(image, (x, y), 10, (0, 255, 255), 10)
            # 
            if "mouse_pts" not in globals():
                mouse_pts = []
                #se agrega el punto obtenido a la variable mause_pts
            mouse_pts.append((x, y))
            # se imprime en consola el arreglo mause_pts
            print("Punto detectado")
            print(mouse_pts)
    '''
    #la siguiente entra se configura dependiendo si se usa un video local, si se puede suprimir
    '''
    # Configuración de entrada de línea de comandos
    parser = argparse.ArgumentParser(description="SocialDistancia")
    parser.add_argument(
        "--videopath", type=str, default="video5.mp4", help="Ruta al archivo de video"
    )
    args = parser.parse_args()

    input_video = args.videopath
    #'''
    # Se define un modelo DNN 
    DNN = model()
    #Se obtine cabezera del video
    #url camara ip
    #url = 'http://192.168.1.102:8080/video'
    #verficar con mas video en linea
    #url = 'https://www.youtube.com/watch?v=7auFijLyiy8&ab_channel=MarqtosPLAY'
    #videos locales
    #cap = cv2.VideoCapture(input_video)
    # abrir un video con url
    #cap = cv2.VideoCapture(url)
    # webcam o camara conectada al pc, 0 es la webcam por defecto
    cap= cv2.VideoCapture(0)
    # varibale para altura del video: si el video tiene una altura de 1280px esta se le asigna a esta variable
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # varible para el ancho del video, si se tiene la altura anterior el ancho sera 720px
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # variable que se le asigna el numero de fotos por segundo del video 
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # se graba 2 video
    #en el primero se sobre ecribe el video original con poligonos marcando las personas
    #el segundo indentifica los objetos y su distnacia 
    #en el segundo video se le reduce la escala con las siguentes variables
    #_W par el ancho: 1280*(1.2/2)=768px
    scale_w = 1.2 / 2
    #_H parel alto:720*(2)=360px
    scale_h = 4 / 2
    #color en rgb para el video de deteccion de objetos
    SOLID_BACK_COLOR = (41, 41, 41 )
    SOLID_BACK_COLOR = (33, 97, 140)
    # Configurar el escritor de video
    #FourCC es un código de 4 bytes que se utiliza para especificar el códec de vídeo. 
    # XVID es un formato de escritura de video
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # como se menciono se escriben dos videos
    # parametros usados: nombreVideo.extension, formato de escritura, numero de fotogramas
    # ancho y alto del video original
    output_movie = cv2.VideoWriter("DetecciónDePeatones.avi", fourcc, fps, (width, height))
    #parametros del segundo video 
    #nombre.extension, formatos de escritura, numero de fotogramas, ango y alto con una escala nueva
    bird_movie = cv2.VideoWriter(
        "Dectector_mov.avi", fourcc, fps, (int(width * scale_w), int(height * scale_h))
    )
    # Se inicializan las variables necesarias
    #numero del fotograma 
    frame_num = 0
    #total de peatones detectados
    total_pedestrians_detected = 0
    # numero de violaciones a la distancia de 180 cm
    total_six_feet_violations = 0
    #pares totales
    total_pairs = 0
    #
    abs_six_feet_violations = 0
    #peatones por secundo
    pedestrian_per_sec = 0
    #
    sh_index = 1
    #
    sc_index = 1
    #crea una ventana con el nombre de image, esta va ser para la eleccion de los 6 puntos
    #cv2.namedWindow("image")
    #se activa la deteccion da la posición de mause y llama la funcion de obtener puntos
    #cv2.setMouseCallback("image", mouse_pts )
    #numero de puntos 
    num_mouse_points = 0
    #crea una variable con valor boleano verdadero
    first_frame_display = True




    # Se procesa cada fotograma, hasta el final del video
    #la varable cap contiene el video
    while cap.isOpened():
        #varible con el numero de fotograma actual aumenta +1 en cada ciclo
        frame_num += 1
        # la funcio readda un valor boleano
        #se inicilaizan 2 variables
        #ambas se les asigna un valor boleano
        #cap.read(), si puede leerelvideo= verdadero si no, pues dara falso
        ret, frame = cap.read()
        #si not es verdadero, la condicion not la niega y convierte en falso
        # al bloque if solo entra si es verdadero
        #si ret es verdadero sigue el while y es falso se para la ejecucion 
        if not ret:
            print("Fin del video...")
            break

        frame_h = frame.shape[0]
        frame_w = frame.shape[1]
        #puesto el al frame_num se le sumo 1 entra al siguiente bloque if
        if frame_num == 1:

    # Pida al usuario que marque puntos paralelos y 
    # dos puntos separados por 180cm aproximadamnete. Orden bl, br, tr, tl, p1, p2  
    #  un ciclo while que siempre se va evaluar como verdadero 
            while True:
                #se inicaliza la varibale image que contiene en fotograma
                # esta imagen sera elprimer fotograma
                # para la eleccion de puntos 
                image = frame
                # se muetrsa una pantalla con el nombre image y la foto
                #o primer fotograma
                cv2.imshow("image", image)
                #espra un milisegunda para que el usario aplate una tecla 
                cv2.waitKey(1)
                # luego de seleccionar los 6 puntos
                # si se hace un nuevo clic 
                # entras al siguiente bloque if
                if len(mouse_pts) == 7:
                    # si se da 7 clicks se cierra la pantalla actual(image)
                    cv2.destroyWindow("image")
                    #rompe el bloque 
                    break
                # le asigna a la variable siguiente un valor falso 
                first_frame_display = False
            #se crea una avriabel y se le asigan el valor de los puntos o cordenadas
            # cabe recordar que es un vector de 1x6   
            four_points = mouse_pts

            # Obtener perspectiva
            # se crea dos varibles con, su perspectiva es los pirmero 4 puntos
            # puesto que con esto selecionaste el area o region de interes
            # ademas se le asigna el primer fotograma de donde se escogio las coordenadas
            M, Minv = get_camera_perspective(frame, four_points[0:4])
            # aregla el vector de 4 putnos y los convierte en escalares
            pts = src = np.float32(np.array([four_points[4:]]))
            '''perspectiveTransformfunciona para conjunto de puntos.
            Aplica la H (Homography o warpMatrix) sobre un conjunto 
            '''
            #se crea un vector con el nombre warpep_pt 
            # se clacula la nueva cordenada con la funciona antes nombrada
            #se alamcena ese nuevo puntos o puntos en el vector de antes
            warped_pt = cv2.perspectiveTransform(pts, M)[0]
            # la función sqrt calcula la raíz cuadrada de cada elemento de la matriz dada.
            # la matriz que se ingresa son lo puntos antes trasformados
            d_thresh = np.sqrt(
                (warped_pt[0][0] - warped_pt[1][0]) ** 2
                + (warped_pt[0][1] - warped_pt[1][1]) ** 2
            )
            # la funcion zeros sirve para la creacion de ceros
            bird_image = np.zeros(
                (int(frame_h * scale_h), int(frame_w * scale_w), 3), np.uint8 
                # uint8, indica que el arreglo no va contener numeros negativos
            )
            #se le asigna el color a lamatriz de objetos detectados
            bird_image[:] = SOLID_BACK_COLOR
            # a la variable detector de peatones de le asigna el fotogramas a nalizar
            pedestrian_detect = frame
        #se imprimer el numero de fotograma que proceso
        print("Procesando fotograma: ", frame_num)
        #se crea un vector con los puntos que van a unirse para formar el poligono
        pts = np.array(
            [four_points[0], four_points[1], four_points[3], four_points[2]], np.int32
        )
        #Se dibuja el polígono de ROI(región binaria de interés
        # se crea un poligono alrededor del objeto detectado
        cv2.polylines(frame, [pts], True, (0, 255, 255), thickness=4)
    
        #Detectar personas y cuadros delimitadores mediante 
        # DNN(Detección de objetos basada en Deep Learning )
        #se crea 2 varibles que contiene a lo peatones detectados, segun el algorigmo DNN
        pedestrian_boxes, num_pedestrians = DNN.detect_pedestrians(frame)
        # si el numero de rectangulos de peatones es mayor a cero entra el bloque if
        # si no hay peatones no hay rectangulos 
        if len(pedestrian_boxes) > 0:
            #se crea la variable detector de peatones
            # se traza el rectangulo en el fotograma 
            pedestrian_detect = plot_pedestrian_boxes_on_image(frame, pedestrian_boxes)
            # se traza los circulos en el video de deteccion de objetos 
            warped_pts, bird_image = plot_points_on_bird_eye_view(
                frame, pedestrian_boxes, M, scale_w, scale_h
            )
            
            six_feet_violations, ten_feet_violations, pairs = plot_lines_between_nodes(
                warped_pts, bird_image, d_thresh
            )
            # el total de peatons detectados se suma con el numero de peatones
            total_pedestrians_detected += num_pedestrians
            #al numero de pares se lesuma su valor que se loincializao con 1
            # osea que al sumarse dara 2, luego 4 ....
            total_pairs += pairs
            # se crea la variable que contiene el numero total de violaciones
            #del distancionamiento socail y se suma con el numero de violaciones
            #a manera de contador, y se divide para el numero de fotograma total
            total_six_feet_violations += six_feet_violations / fps
            # aqui se calcula el indice de que salen de casa 
            # esto puede ayudar a realizar futuros calculos probabilisticos
            abs_six_feet_violations += six_feet_violations
            pedestrian_per_sec, sh_index = calculate_stay_at_home_index(
                total_pedestrians_detected, frame_num, fps
            )
        # variables numericas usadas mas adelante
        aux=0
        last_h = 75
        
        text = "# 180cm violaciones: " + str(int(total_six_feet_violations))
        #print(total_six_feet_violations)
       
        #imprime el texto en pantalla
        pedestrian_detect, last_h = put_text(pedestrian_detect, text, text_offset_y=last_h)
        t=int(total_six_feet_violations)
        if count ==t :
            alarmaE();
            count+=1
            print(count)

        '''
        text = "IndicePer: " + str(np.round(100 * sh_index, 1)) + "%"
        pedestrian_detect, last_h = put_text(pedestrian_detect, text, text_offset_y=last_h)

        if total_pairs != 0:
            sc_index = 1 - abs_six_feet_violations / total_pairs

        text = "IDistanciamiento: " + str(np.round(100 * sc_index, 1)) + "%"
        pedestrian_detect, last_h = put_text(pedestrian_detect, text, text_offset_y=last_h)
        '''
        #crea una pantalla con ese nombre 
        cv2.imshow("Deteccion en tiempo real", pedestrian_detect)
        cv2.waitKey(1) 
        output_movie.write(pedestrian_detect)
        bird_movie.write(bird_image)

