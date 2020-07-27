import cv2 
import numpy as np

images = [] 


try:
    panoramica = cv2.imread('teste.png')
    images.append(panoramica)

except cv2.error as e:
    pass






try:
    for i in range(1,3): #carregando as imagens 
        image = cv2.imread('./output/ajusted{}.png'.format(i))

        height = np.size(image, 0)
        width = np.size(image,1)

        image = cv2.resize(image,(width,height))
        print('Adicionando a image',i,' à lista de images')
        images.append(image)

        try:
            #junção
            stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)#criando a costura
            rat, pan = stitcher.stitch(images) #costurando as imagens
            horizontal = cv2.flip(pan,1) #corrigindo o efeito espelho
            cv2.imwrite('teste.png', horizontal) #salvando ima
            #---
        except cv2.error as e:
            print('nao deu...',e)
            pass

        i = i + 1

except cv2.error as e:
    print('\nInvalid frame!\n', e)
cv2.waitKey()

