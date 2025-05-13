import cv2 as cv

imagen = cv.imread("tung.jpeg", 0) # lee la imagen en blanco y negro

imagen_sin_color = cv.imwrite("img_sin_color.png", imagen) # Guarda la imagen como un nuevo archivo
cv.imshow("Italian brianrot", imagen) # Muestra una ventana con la imagen
cv.waitKey(0) # Abre la ventana por tiempo infinito
cv.destroyAllWindows() #Cierra opencv

