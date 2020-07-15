
import numpy as np
import cv2
import sys

# FIXME: Erro na imagem do chão.


def floor():
    size = (1080,720) #definindo futuro tamanho de imagem
    try: #carregando as imagens
        centro = cv2.imread('./exe1/1.png')
        centro = cv2.resize(centro, size)
        centro = cv2.rotate(centro, cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        close = cv2.imread('./exe1/close.png')
        close = cv2.resize(close,size)
        close = cv2.rotate(close, cv2.ROTATE_90_COUNTERCLOCKWISE)

        chao = cv2.imread('./exe1/chao.png')
        chao = cv2.resize(chao,size)
        chao = cv2.rotate(chao, cv2.ROTATE_90_COUNTERCLOCKWISE)

    except cv2.error as e:
        print('Invalid frame!\n\n', e)
    cv2.waitKey()

    
    images = []  #colocando as imagens em um array
    images.append(centro)
    images.append(close)
    images.append(chao)

    stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)#criando a costura
    rat, pan = stitcher.stitch(images) #costurando as imagens
    
    try: #retornando a imagem
        cv2.imshow('Imagem criada', pan) #mostrando a imagemcv2.imshow('Imagem criada', centro) #mostrando a imagem
        cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
        cv2.imwrite('withFloor.png', pan) #salvando imagem na mesma pasta do script
    except cv2.error as e:
        print('Algo deu errado, tente novamente\n\n',e)
        cv2.waitKey()
    

floor()