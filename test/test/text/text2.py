with open(".\dataset_3363_3.txt") as inf:
    st = inf.readline().strip()

# st = "abc a bCd bC AbC BC BCD bcd ABC"
s = [i.lower() for i in st.split()]
print (st)
print (s)

def f(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

d = f(s)

maxI = 0
maxL= ''
for key, value in d.items():
    if (value > maxI or (value == maxI and key < maxL)):
        maxI = value
        maxL = key

print (maxL, maxI)
