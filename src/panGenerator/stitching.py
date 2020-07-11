import numpy
import cv2
import cv2 as cv


#carregando as imagens
try:
    first = cv.imread('esquerda.jpg')
    second = cv.imread('direita.jpg')
except cv.error as e:
    print('Invalid frame!\n\n', e)
cv.waitKey()

#colocando as imagens em um array
images = []  
images.append(first)
images.append(second)

stitcher = cv.Stitcher.create()
rat,pan = stitcher.stitch(images)

if rat == cv.Stitcher_OK:
    cv.imshow('Imagem criada', pan)
    cv.waitKey()
    cv.destroyAllWindows()
else:
    print('ddd')