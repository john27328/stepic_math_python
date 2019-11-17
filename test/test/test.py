#your code
a = 2
b = 3
L = [1, 2, 6]
for i in range(len(L)-1):
    if(abs(L[i] - L[i+1]) == 1): 
        print(i, L[i] - L[i+1])
        index = i

print(index)