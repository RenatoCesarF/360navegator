
import numpy as np
import cv2
import sys

# FIXME: Erro na imagem do chão.
def floor(namePan):
    size = (1080,720) #definindo futuro tamanho de imagem
    try: #carregando as imagens
        centro = cv2.imread('./exe1/1.png')
        centro = cv2.resize(centro, size)

        chao = cv2.imread('./exe1/chao.png')
        chao = cv2.resize(chao,size)

    except cv2.error as e:
        print('Invalid frame!\n\n', e)
    cv2.waitKey()


    images = []  #colocando as imagens em um array
    images.append(chao)
    images.append(centro)


    stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)#criando a costura
    rat, pan = stitcher.stitch(images) #costurando as imagens


    try: #retornando a imagem
        cv2.imshow('Imagem criada', pan) #mostrando a imagem
        cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
        cv2.imwrite(namePan, pan) #salvando imagem na mesma pasta do script
        
    except cv2.error as e:
        print('Algo deu errado, tente novamente\n\n',e)
        cv2.waitKey()


floor('Panoramica.png')