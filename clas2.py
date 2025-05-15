import cv2 as cv 
import os

capture = cv.VideoCapture(0) # Inicia la captura de video 
salida = cv.VideoWriter("video1.mp4", frameSize=(640,480), fps=20, fourcc=cv.VideoWriter_fourcc(*"mp4v"))
while (capture.isOpened()): # Si la imagen esta abierta debe iniciar un bucle
    ret, imagen = capture.read() # Lee el frame del stream
    if ret == True: #Si hay un frame disponible lo muestra 
        cv.imshow("video", imagen)
        salida.write(imagen)
        if cv.waitKey(1) & 0xFF == ord('q'): # Si haces click en q puedes cerrar la ventana
            break
    else: break
capture.release() #libera el proceso de la imagen 
salida.release()
cv.destroyAllWindows() #eliminan las ventanas abierta de opencv
os.system("video1.mp4")