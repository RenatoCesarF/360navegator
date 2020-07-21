'''
Este é o script principal do programa, é aqui que a "magia"
acontece. Usando openCV o programa pega diversa fotos, do mesmo
ambiente, da pasta output e as transforma em uma foto só. Quanto
mais fotos melhor.


TODO: ver se é possível fazer duas panoramicas, uma do chao e uma do teto
e ai junta-las depois
'''

import numpy as np
import cv2


def stitch(images):
    stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)#criando a costura
    rat, pan = stitcher.stitch(images) #costurando as imagens
    return pan

    
def sideToSide(namePan,horizontal):
    horizontal = horizontal + 1
    images = [] # Array de imagens 
    #1366,786
    size = (1920,1080) #definindo futuro tamanho das imagens
    try: 

        for i in range(1,horizontal): #carregando as imagens (da primeira à quinta)
            image = cv2.imread('./output/test{}.png'.format(i))
            print('Adicionando a image',i,' à lista de images')
            image = cv2.resize(image, size)
            images.append(image)

            i = i + 1

    except cv2.error as e:
        print('\nInvalid frame!\n', e)
    cv2.waitKey()

    pan = stitch(images)


    try: #retornando a imagem
        horizontal = cv2.flip(pan,1) #corrigindo o efeito espelho
        cv2.imwrite(namePan, horizontal) #salvando imagem na mesma pasta do script            
        cv2.imshow('Imagem criada', horizontal) #mostrando a imagem
        cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
      
        
    except cv2.error as e:
        print('\nAlgo deu errado, tente novamente\n\n',e)
        cv2.waitKey()
 

sideToSide('horizontal.png',17)