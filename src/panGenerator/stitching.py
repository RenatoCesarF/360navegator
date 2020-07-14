
import numpy as np
import cv2
import sys
#from fishLen import addFish


size = (1080,720) #definindo futuro tamanho de imagem
try: #carregando as imagens
    primeira = cv2.imread('1.png')
    primeira = cv2.resize(primeira, size)

    segunda = cv2.imread('2.png')
    segunda = cv2.resize(segunda,size)

    terceira = cv2.imread('3.png')
    terceira = cv2.resize(terceira,size)

    quarta = cv2.imread('4.png')
    quarta = cv2.resize(quarta,size)

    quinta = cv2.imread('5.png')
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




stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)
rat,pan = stitcher.stitch(images)


try:
    cv2.imshow('Imagem criada', pan) #mostrando a imagem
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("novaPanoramica.png",pan) #salvando imagem na mesma pasta dp script
    

except cv2.error as e:
    print('Algo deu errado, tente novamente\n\n',e)
    cv2.waitKey()
    
cv2.waitKey()
sys.exit()