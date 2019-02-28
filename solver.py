from parser import parse
import numpy as np

file = "files/a_example.txt"
num_fotos, fotos = parse(file)


def matriz_vertical():
    verticales = fotos["V"]
    num_verticales = len(verticales)
    mat_v = np.zeros((num_verticales, num_verticales))

    c1 = 0
    for key, foto in verticales.items():
        c2 = 0
        for key2, foto2 in verticales.items():
            comunes = set(foto) | (set(foto2))
            mat_v[c1][c2] = len(comunes)
            c2 +=1
        c1 +=1

    return mat_v
