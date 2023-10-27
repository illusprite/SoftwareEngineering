from math import sqrt
def Heron(a, b, c):
    p = (a+b+c)/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    print(S)