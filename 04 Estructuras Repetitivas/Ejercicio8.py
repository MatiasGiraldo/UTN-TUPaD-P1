i = 1
pos = 0
neg = 0
par = 0
impar = 0
cant = 5
while i <= cant:
    num = int(input(f"Ingrese numero {i}: "))
    i += 1
    if num < 0 :
        if num % 2 == 0:
            neg += 1
            par += 1
        else:
            neg += 1
            impar +=1
    else:
        if num % 2 == 0:
            pos += 1
            par += 1
        else:
            pos += 1
            impar +=1
print(f"{pos} son positivos")
print(f"{neg} son negativos")
print(f"{par} son pares")
print(f"{impar} son impares")