import numpy as np
import cv2
'''
FIXME: 1, tirar mais fotos pra tentar junta-las aqui de novo, 
        do chão, junto com a panoramica horizontal

'''


def stitch(images):
    stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)#criando a costura
    rat, pan = stitcher.stitch(images) #costurando as imagens
    return pan

    
def sideToSide(namePan):
 
    images = [] # Array de imagens 
    #1366,786
    size = (800,600) #definindo futuro tamanho das imagens
    try: 

        for i in range(1, 8): #carregando as imagens (da primeira à quinta)
            image = cv2.imread('./exe2/output/test{}.png'.format(i))
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
 

sideToSide('panoramica.png')