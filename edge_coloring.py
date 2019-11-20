# a = [
#     [2,0],
#     [0,1]
# ]


def initializeMatrix(m):
    newm = []
    i = 0
    while i < len(m):
        newm.append([]);
        j = 0
        while j < len(m[i]):
            if m[i][j]==0:
                newm[i].append(0)
            else:
                newm[i].append(1)
            j += 1
        i += 1
    return newm

# print(initializeMatrix(a))



def initSquareMatrix(n):
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(0)
    return mat



# b0 = [
#     [1,1,1],
#     [1,0,1],
#     [1,1,0]
# ]


b = [
    [2,1,0,1],
    [1,0,1,0],
    [0,1,0,3],
    [1,0,3,0]
]

def findGraphColoring(m):
    keycols = initSquareMatrix(len(m))
    colverts = []
    coln = 0;
    for i in range(len(m)):
        colverts.append({})
        # making color hash for column
        # initializing matrices

    for i in range(len(m)):
        # col = 1
        for j in range(i+1):# including the loopback
            # loop through row. no same color
            if m[i][j] == 0:
                continue


            col = 1
            while True:
                if (not col in colverts[i]) and (not col in colverts[j]):
                    colverts[i][col] = 1
                    colverts[j][col] = 1
                    keycols[i][j] = col
                    keycols[j][i] = col
                    break
                else:
                    col += 1
                    if col > coln: coln = col
#     print(coln)
    return [keycols,coln]

def separateColors(colmat,n,original):
    retvals = []
    for col in range(1,n+1):
        onecolmat = initSquareMatrix(len(colmat))
        for i in range(len(colmat)):
            for j in range(len(colmat)):# including the loopback
                if col == colmat[i][j]:
                    onecolmat[i][j] = original[i][j]
        retvals.append(onecolmat)
    return retvals

def GCL(m):
    colset = findGraphColoring(initializeMatrix(m))
    colmat = colset[0]
    colnum = colset[1]
    return separateColors(colmat, colnum, m)





# print(findGraphColoring(b))
# print(GCL(b))
