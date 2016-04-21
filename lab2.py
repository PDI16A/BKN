import os, os.path, sys
from SimpleCV import *
import matplotlib.pyplot as plt
import time
import pip 
from sklearn import preprocessing
from sklearn.cluster import KMeans
import argparse
import utils
import cv2



#### CAPTURAR IMAGEN #####
c = Camera()
plt.ion()
time.sleep(2)

img = c.getImage()
#img.save("fotTTo.jpg")
#img.show()

#### OBTENER HISTOGRAMA ####
#img=Image("fotTTo.jpg")

gray = img.toGray()
#gray.save("fotTTo_gray.jpg")
#hist = gray.histogram(255)
#plt.plot(hist)
#plt.pause(-1)

#### DIVISION DE COLORES #####

#(red, green, blue) = img.splitChannels(False)
#red_hist = red.histogram(255)
#green_hist = green.histogram(255)
#blue_hist = blue.histogram(255)

## Guardamos las imagenes ##
#red.save("fotTTo_red.jpg")
#green.save("fotTTo_green.jpg")
#blue.save("fotTTo_blue.jpg")


#plt.plot(blue_hist)
#plt.pause(-1)

#### SEGMENTAR 	DE FORMA MANUAL ####
## LETRAS
#img1 = gray.binarize(105)
#img1.save("fotTTo_img1.jpg")
#imLetras = gray*img1
#imLetras.save("1.jpg")

## FONDO
#img2 = gray.binarize(110)
#img3  = img2.invert()
#img3.save("fotTTo_img2.jpg")
#imFondo = gray*img3
#imFondo.save("2.jpg")

## CUADRICULAS
#img4 = gray.binarize(193)
#img4.save("fotTTo_img3.jpg")
#imFondo = gray*img4
#imFondo.save("3.jpg")

#### SEGMENTAR Kmeans ####

img5 = gray.binarize(131.9116)
img5.save("fotTTo_img4.jpg")

#img4 = gray.binarize(61.4836711)
#img4.save("fotTTo_img5.jpg")

