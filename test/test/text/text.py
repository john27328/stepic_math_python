with open(".\dataset_3363_2.txt") as inf:
    s = inf.readline().strip()

print(s)

i = 0
num = [str(i) for i in range(10)]
res = ""
while i < len(s):
    c = s[i]
    i = i+1
    tmp = ""
    while i < len(s) and s[i] in num:
        tmp += s[i]
        print(c, tmp)
        i = i+1
    l = int(tmp)
    res += c * l

print(res)
            