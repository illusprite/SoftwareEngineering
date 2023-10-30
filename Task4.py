x = input("Введите предложение: ")

with open("input.txt", "r") as file:
    prohibited = file.read().split(" ")

for zap in prohibited:
    while zap in x.lower():
        ct = len(zap)*'*'
        b = x.lower().index(zap)
        x = x.replace(x[b:b+len(zap)], ct)
print(x)


