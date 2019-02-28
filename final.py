from parser import parse
import numpy as np



def matriz_vertical():
    verticales = fotos["V"]
    num_verticales = len(verticales)
    if num_verticales == 0:
        return []
    mat_v = np.zeros((num_verticales, num_verticales))

    c1 = 0
    for key, foto in verticales.items():
        c2 = 0
        for key2, foto2 in verticales.items():
            comunes = set(foto) | (set(foto2))
            mat_v[c1][c2] = len(comunes)
            c2 +=1
        c1 +=1
    return np.matrix(mat_v)


def maximo_vertical(mat_v):
    maximos_v = []
    vertical = fotos["V"]
    lista_v = list(vertical)
    while mat_v.max() >= 0:
        result = np.where(mat_v == np.max(mat_v))
        x = result[0][0]
        y = result[1][0]
        #valor = mat_v[x ,y]
        mat_v[x,:] = -np.inf
        mat_v[:,y] = -np.inf
        mat_v[y,:] = -np.inf
        mat_v[:,x] = -np.inf
        foto1 = lista_v[x]
        foto2 = lista_v[y]
        pareja = [foto1, foto2]
        maximos_v.append(pareja)
    return maximos_v


def generateValue(album, slide1, slide2):
    if slide1 != -1 and slide2 != -1:

        if type(slide1) is int:
            list1 = album["H"][slide1]
        else:
            list1 = list(set(album["V"][slide1[0]] + album["V"][slide1[1]]))

        if type(slide2) is int:
            list2 = album["H"][slide2]
        else:
            list2 = list(set(album["V"][slide2[0]] + album["V"][slide2[1]]))

        intersection = len(list(set(list1) & set(list2)))
        diff1 = len(list(set(list1) - set(list2)))
        diff2 = len(list(set(list2) - set(list1)))

        return min(intersection, diff1, diff2)
    return -1


def slideComb(album, Vlist):
    matSlides = []
    sList = []
    for i in range(num_fotos):
        sList.append(-1)
        matSlides.append([])
        for j in range(num_fotos):
            matSlides[i].append(-1)

    for key in album["H"]:
        sList[key] = key

    for i in range(len(Vlist)):
        sList[Vlist[i][0]] = Vlist[i]

    for i in range(num_fotos):
        for j in range(num_fotos):
            if i != j:
                matSlides[i][j] = generateValue(album, sList[i], sList[j])

    return matSlides, sList

def slideShow(matS, listS, tallaRes):
    res = []
    already = []
    coord_max = np.where(matS == np.max(matS))
    x = coord_max[0][0]
    already.append(x)
    y = coord_max[1][0]
    while len(already) < tallaRes:
        max = -1
        auxi = -1
        for i in range(num_fotos):
            if matS[i][y] > max and i not in already:
                max = matS[i][y]
                auxi = i
        already.append(y)
        y = auxi

    for element in already:
        res.append(listS[element])

    return res

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



if __name__ == '__main__':
    file = "files/b_lovely_landscapes.txt"
    num_fotos, fotos = parse(file)
    print("Generando matriz vertical:")
    matV = matriz_vertical()
    print("Matriz vertical generada.")
    if len(matV) == 0:
        print("Sin maximo vertical:")
        emparejamientos = []
    else:
        print("Generando emparejamientos verticales:")
        emparejamientos = maximo_vertical(matV)

    print("Emparejamientos realizados")
    N = len(fotos['H']) + len(emparejamientos)
    print("Generando matriz de slides:")
    matS, listS = slideComb(fotos, emparejamientos)
    print("Matriz de slides generada.")
    print("Generando SlideShow:")
    res = slideShow(matS, listS, N)
    print("Fini.")
    resultado(res, 'outB.txt')


