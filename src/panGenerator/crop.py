'''
Esta função serve apenas para cortar determinada
porcentagem da imagem caso seja necessário,
na maioria das vezes não é
'''

import cv2  
import numpy as np


def crop():
    try: #carregando as imagens
        img = cv2.imread('Panoramica.png')
    except cv2.error as e:
        print('Invalid frame!\n\n', e)
    cv2.waitKey()

    
    imgHeight = img.shape[0] 

    startHeight = int(imgHeight * 0.10)    # começa em 10% da imagem
    finalHeight = int(imgHeight * 0.90) # Termina em 90% da imagem

    #Recortando a imagem
    croped = img[startHeight:finalHeight, 0:img.shape[1]]

    try:
        cv2.imshow('Imagem criada', croped) #mostrando a imagem
        cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
        cv2.imwrite('croped.png', croped) #salvando imagem na mesma pasta do script
        
    except cv2.error as e:
        print('\n Algo de errado aconteceu tente novamente \n',e)



crop()


