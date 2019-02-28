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

def maximo_vertical():
    maximos_v = []
    vertical = fotos["V"]
    lista_v = list(vertical)
    mat_v = matriz_vertical()
    mat_v = np.matrix(mat_v)
    while mat_v.max() >= 0:
        result = np.where(mat_v == np.max(mat_v))
        x = result[0][0]
        y = result[1][0]
        #valor = mat_v[x ,y]
        mat_v[x] = -np.inf
        mat_v[y] = -np.inf
        foto1 = lista_v[x]
        foto2 = lista_v[y]
        pareja = [foto1, foto2]
        maximos_v.append(pareja)

    return maximos_v
