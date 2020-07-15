import numpy as np
import cv2


#FIXME: caso resolva usar esse metodo
# Fazer uma mascara gerada automaticamente

def paint():
    try: #carregando as imagens
        img = cv2.imread('Panoramica.png')
        
        mask = cv2.imread('./exe1/mask.png',0)

    except cv2.error as e:
        print('Invalid frame!\n\n', e)
    cv2.waitKey()

    painted = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

    try: #retornando a imagem
        cv2.imshow('pintada', painted) #mostrando a imagem
        cv2.imwrite('painted.png', painted)
        cv2.waitKey() #assim que alguma tecla for pressionada as imagem se fecha
        #cv2.imwrite(namePan, espelhada) #salvando imagem na mesma pasta do script
        
    except cv2.error as e:
        print('Algo deu errado, tente novamente\n\n',e)
        cv2.waitKey()


paint()
