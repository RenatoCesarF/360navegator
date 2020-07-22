# Este script renomeia as imagens de input para serem imagens com nomes de 0 a x
import os
from glob import glob
number = 15
for number , filename in enumerate(glob("./input/*.jpg")):
    try:
        os.rename(filename, "./input/{0}.jpg".format(number))
    except OSError as e:
        print("Something happened:", e)

