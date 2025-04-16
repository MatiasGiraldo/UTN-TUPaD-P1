import random
rand = random.randint(0,9)
num = int(input("Ingrese numero: "))
intento = 1
while num != rand:
    num = int(input("Ingrese numero: "))
    intento = intento + 1
print(f"El numero de intentos fue {intento}")