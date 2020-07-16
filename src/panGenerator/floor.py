
import numpy as np
import cv2
import sys
'''
 FIXME: as imagens mudam de tamanho, ou seja, teria que fazer um jeito
        de contornar isso, ou fazendo primeiro uma dupla, uma do chão
        depois uma na horizontal e depois sim juntar todas elas (testar novas fotos)
      
'''
def stitch(array):
    stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)#criando a costura
    rat, final = stitcher.stitch(array) #costurando as imagens
    final = cv2.rotate(final, cv2.ROTATE_90_CLOCKWISE)
    return final

def floor():

    images = []  #colocando as imagens em um array
    side = []
    final = []

    size = (1080,720) #definindo futuro tamanho de imagem
    try: #carregando as imagens
        
        centro = cv2.imread('./exe1/horizontal/1.png')
        centro = cv2.resize(centro,size)
        centro = cv2.rotate(centro, cv2.ROTATE_90_COUNTERCLOCKWISE)
        images.append(centro)
        
        close = cv2.imread('./exe1//horizontal/5.png')
        close = cv2.resize(close,size)
        close = cv2.rotate(close, cv2.ROTATE_90_COUNTERCLOCKWISE)
        images.append(close)

        final = stitch(images)

    except cv2.error as e:
        print('Invalid frame!\n\n', e)
        pass
    cv2.waitKey()

    
    

    try: #retornando a imagem
        cv2.imshow('Imagem criada', final) 
        cv2.imwrite('./exe1/saidas/out2.png', final) #salvando imagem na mesma pasta do script
        cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
    except cv2.error as e:
        print('Algo deu errado, tente novamente\n\n',e)
        cv2.waitKey()   
 

floor()