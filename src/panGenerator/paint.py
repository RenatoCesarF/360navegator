'''
Usando da função inrange, este script faz
uma mascara preto-e-branco onde todas as partes
onde a imagem for 100% preto, na mascara serão 
brancas, aplica-se então essa mascara em cima da 
imagem normal, a função inpaint tenta completar a 
imagem de acordo com a mascara, repintando as partes
brancas da mascara.
'''

import numpy as np
import cv2

def blackParts(panoramica):
    def paint(image):
        try:
            image = cv2.imread(image)
            mask = cv2.imread('mask.png',0)
        except cv2.error as e:
            print(e)
        cv2.waitKey()

        print('...Pintando...')
        painted = cv2.inpaint(image,mask,3,cv2.INPAINT_TELEA)

        try: #retornando a imagem
            print('\nImagem repintada\n')
            cv2.imwrite('painted.png', painted)
            cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
            print('\nImagem repintada\n')
            
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
            imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #esse ultimo parametro transforma a imagem em preto e branco, testar sem ele.
            lower = np.array(myColor[0:3])
            upper = np.array(myColor[3:6])
            mask = cv2.inRange(imgHSV,lower,upper)
            cv2.imwrite("mask.png",mask)
            print('\nMascara criada\n')
        except cv2.error as e:
            print(e)


    mkMask(panoramica)
    paint(panoramica)
    