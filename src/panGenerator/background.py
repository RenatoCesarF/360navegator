import cv2
import utils



for i in range(1,6):
    nameFile = '{}.png'.format(i)

    path = './exe1/horizontal/{}'.format(nameFile)
    frame = cv2.imread("./exe2/regua.png")

    try:   
        image = cv2.imread(path)
    
    except cv2.error as e:
        print(e)


    x_offset = 170
    w_ = frame.shape[1] - x_offset
    h_ = w_ * (image.shape[0] / image.shape[1])
    y_offset = int(frame.shape[0] - h_) // 2


    image = cv2.resize(image, (int(w_), int(h_)))
    frame[y_offset:y_offset+image.shape[0], x_offset:x_offset+image.shape[1]] = image

    cv2.imwrite('./exe2/output/teste{}.png'.format(i), frame)

    i = i + 1











