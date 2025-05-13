import cv2 as cv 

capture = cv.VideoCapture(0) # Inicia la captura de video 

while (capture.isOpened()): # Si la imagen esta abierta debe iniciar un bucle
    ret, imagen = capture.read() # Lee el frame del stream

    if ret == True: #Si hay un frame disponible lo muestra 
        cv.imshow("video", imagen)
        if cv.waitKey(0) & 0xFF == ord('q'): # Si haces click en q puedes cerrar la ventana
            break
        else:
            break
capture.release() #libera el proceso de la imagen 
cv.destroyAllWindows() #eliminan las ventanas abierta de opencv
            