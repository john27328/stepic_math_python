#your code
L = ['Aa', 'ABBA', 'ab', 'AaAa', 'AaAaAa']

def counter(T):
    ncList = []
    ncmax = 0
    for i, v in enumerate(T):
        cList = []
        v = v.lower()
        ncList.append(0)
        for c in v: 
            if(not c in cList):
                ncList[i] = ncList[i] + 1
                cList.append(c)
        if (ncList[i] > ncmax):
            ncmax = ncList[i]
    lenMax = 0
    for i, v in enumerate(ncList):
        if (v == ncmax):
            if(len(T[i]) > lenMax):
                lenMax = len(T[i])
    return lenMax

print counter(L)

 