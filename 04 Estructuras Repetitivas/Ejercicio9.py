i = 1
suma = 0
cant = 5
while i <= cant:
    num = int(input(f"Ingrese numero {i}: "))
    suma += num
    i += 1
print(f"El promedio es {suma/cant}")