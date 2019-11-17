#your code
a = 2
b = 3
def sum2(a, b):
    if(type(a) in (int, float) and type(b) in (int, float)): 
        return a + b
    if(type(b) in (int, float)): 
        return "1st argument is not a number"
    if(type(a) in (int, float)): 
        return "2nd argument is not a number"
    return "all arguments are not a numbers"

print(sum2(a,b))