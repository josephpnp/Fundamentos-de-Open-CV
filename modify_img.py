import cv2 as cv

imagen = cv.imread('tung.jpeg')
cv.line(imagen, (250,250), (250,250), (255,0,0),10,)
cv.line(imagen, (350,250), (350,250), (255,0,0),10,)
cv.line(imagen, (250,150), (250,150), (255,0,0),10,)
cv.line(imagen, (150,250), (150,250), (255,0,0),10,)
cv.line(imagen, (200,350), (200,350), (255,0,0),10,)
cv.line(imagen, (300,350), (300,350), (255,0,0),10,)

cv.line(imagen, (250,150),(200,350), (255,0,0),10,)
cv.line(imagen, (250,150),(300,350), (255,0,0),10,)
cv.line(imagen, (350,250),(150,250), (255,0,0),10,)
cv.line(imagen, (300,350),(150,250), (255,0,0),10,)
cv.line(imagen, (200,350),(350,250), (255,0,0),10,)

cv.imshow("italian brainrot", imagen)

cv.waitKey(0)
cv.destroyAllWindows()