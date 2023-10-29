from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
def Heron(a, b, c):
    p = (a+b+c)/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    return S
print(f"S первого треугольника: {Heron(max(one), max(two), max(three))} \n"
      f"S второго треугольника: {Heron(min(one), min(two), min(three))} \n")
print(f"Максимальные стороны: {max(one), max(two), max(three)} \n"
      f"Минимальные стороны: {min(one), min(two), min(three)} \n")
