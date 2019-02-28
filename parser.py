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
            print(foto)
            orientacion = foto[0]
            tags = foto[2:]

            fotos[orientacion][i] = tags

        print (fotos)
        return N, fotos
