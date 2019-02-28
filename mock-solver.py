def generateValue( album, slide1, slide2):

    if slide1 != -1 and slide2!=-1:

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

        return min(intersection,diff1,diff2)
    return -1
    

def slideComb(album,Vlist):

    matSlides = []
    sList = []
    for i in range(N):
        sList.append(-1)
        matSlides.append([])
        for j in range(N):
            matSlides[i].append(-1)
        

    for key in album["H"]:
        sList[key]=key
    
    for i in range(len(Vlist)):
        sList[Vlist[i][0]] = Vlist[i]

    for i in range(N):
        for j in range(N):
            if i != j:
                matSlides[i][j] = generateValue(album, sList[i],sList[j])

    return matSlides, sList



N=4
album={'H': {0: ['cat', 'beach', 'sun'], 3: ['garden', 'cat']}, 'V': {1: ['selfie', 'smile'], 2: ['garden', 'selfie']}}
Vlist=[[1,2]]

matSlides, sList = slideComb(album,Vlist)

print(matSlides)


