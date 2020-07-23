# Este script renomeia as imagens de input para serem imagens com nomes de 0 a x
import os
import os.path
from glob import glob

def rename():
    print('\nRenomeando...\n')
    for number , filename in enumerate(glob("./input/*.*")):
        try:
            os.rename(filename, "./input/{0}.png".format(number))
        except OSError as e:
            print("Something happened:", e)

rename()