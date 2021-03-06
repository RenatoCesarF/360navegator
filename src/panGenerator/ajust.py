'''
Este script aplica um fundo preto em todas as imagens da pasta 
"input" e as coloca na pasta "output", esse processo evita pro_
blemas de redimensionamento que o programa pode achar durante os
processo.

'''
import glob
import cv2
import os


def ajust(amount):
    print('\n Ajustando imagens...\n')
    for i in range(1,amount):
        nameFile = '{}.jpg'.format(i)
        path = './input/{}'.format(nameFile)
        print('imagem {} ajustada'.format(i))
        frame = cv2.imread("1920.png")
        # Essa imagem "frame" é o background em todas
        # as nossas imagens, quanto maior a qualidade dela melhor a qualidade
        # final da nossa panoramica. Ela é preta pelo motivo de termos um 
        # script que completa brexas pretas da imagem, que pode ser aplicado
        # na panoramica final.

        try:   
            image = cv2.imread(path)
        
        except cv2.error as e:
            print(e)


        x_offset = 5
        w_ = frame.shape[1] - x_offset
        h_ = w_ * (image.shape[0] / image.shape[1])
        y_offset = int(frame.shape[0] - h_) // 2



        image = cv2.resize(image, (int(w_), int(h_)))
        frame[y_offset:y_offset+image.shape[0], x_offset:x_offset+image.shape[1]] = image

        cv2.imwrite('./output/ajusted{}.png'.format(i), frame)

        i = i + 1
        

def count():
    amount = 0
    for f in glob.glob('./input/*.*'):
        amount = amount + 1

    print(amount,'arquivos no total no diretório')
    return amount

quantidade = count()
ajust(quantidade)
