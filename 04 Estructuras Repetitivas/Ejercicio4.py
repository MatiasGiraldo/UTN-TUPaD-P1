suma = 0
i = 1
while i != 0:
    num = int(input("Ingrese numero enteroa sumar: "))
    suma = suma + num
    print("Si desea salir del programa y ver el resultado, ingrese 0, de lo contrario ingrese cualqueir otra cosa:")
    i = int(input())
print(f"El total acumulado es {suma}")