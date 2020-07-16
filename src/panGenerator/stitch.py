import numpy as np
import cv2



def sideToSide(namePan):
    size = (1366,768) #definindo futuro tamanho de imagem
    try: #carregando as imagens
    
                            #Caminho da iamgem
        primeira = cv2.imread('./exe1/1.png')
        primeira = cv2.resize(primeira, size)
        
        segunda = cv2.imread('./exe1/2.png')
        segunda = cv2.resize(segunda,size)

        terceira = cv2.imread('./exe1/3.png')
        terceira = cv2.resize(terceira,size)

        quarta = cv2.imread('./exe1/4.png')
        quarta = cv2.resize(quarta,size)

        quinta = cv2.imread('./exe1/5.png')
        quinta = cv2.resize(quinta, size)

    except cv2.error as e:
        print('Invalid frame!\n\n', e)
    cv2.waitKey()


    images = []  #colocando as imagens em um array
    images.append(primeira)
    images.append(segunda)
    images.append(terceira)
    images.append(quarta)
    images.append(quinta)


    stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)#criando a costura
    rat, pan = stitcher.stitch(images) #costurando as imagens


    try: #retornando a imagem
        espelhada = cv2.flip(pan,1) #corrigindo o efeito espelho
        cv2.imshow('Imagem criada', espelhada) #mostrando a imagem
        cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
        cv2.imwrite(namePan, espelhada) #salvando imagem na mesma pasta do script
        
    except cv2.error as e:
        print('Algo deu errado, tente novamente\n\n',e)
        cv2.waitKey()


sideToSide('PanoramicaWithPainting.png')
