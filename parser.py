import math
import random
import sys


def parse(file):
    diccionario = {}
    fotos = {}
    fotos["H"] = {}
    fotos["V"] = {}

    with open(file) as f:
        N = int(f.readline())
        diccionario["num_fotos"] = N
        for i in range(N):
            foto = f.readline().strip().split(" ")
            orientacion = foto[0]
            tags = foto[2:]
            fotos[orientacion][i] = tags

    return N, fotos

def resultado(resultados, file):
    with open(file, "w") as f:
        f.write(str(len(resultados)) + "\n")
        for item in resultados:
            if type(item)== list:
                for i in item:
                    r = str(item[0]) + " " + str(item[1])
            else:
                r = str(item)
            f.write(r + "\n")
