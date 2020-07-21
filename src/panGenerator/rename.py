# Este script renomeia as imagens de input para serem imagens com nomes de 0 a x
import os
from glob import glob

for number, filename in enumerate(glob("./input/*.png")):
    try:
        os.rename(filename, "./input/{0}.png".format(number))
    except OSError as e:
        print("Something happened:", e)

