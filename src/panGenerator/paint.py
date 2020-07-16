import numpy as np
import cv2

def paint(image):
    try:
        image = cv2.imread(image)
        mask = cv2.imread('mask.png',0)
    except cv2.error as e:
        print(e)
    cv2.waitKey()


    painted = cv2.inpaint(image,mask,3,cv2.INPAINT_TELEA)

    try: #retornando a imagem
        cv2.imshow('pintada', painted) #mostrando a imagem
        cv2.imwrite('painted.png', painted)
        cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
        
    except cv2.error as e:
        print('Algo deu errado, tente novamente\n\n',e)
        cv2.waitKey()

def mkMask(image):

    try:
        img = cv2.imread(image)
    except cv2.error as e:
        print(e)

    myColor = [ 0,0,0,0,0,0]

    try:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array(myColor[0:3])
        upper = np.array(myColor[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        cv2.imwrite("mask.png",mask)
    except cv2.error as e:
        print(e)

panoramica = 'cilynder.jpg'

mkMask(panoramica)
paint(panoramica)


