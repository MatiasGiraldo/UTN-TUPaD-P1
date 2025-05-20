def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)

n = int(input("Ingrese base: "))
if n >= 1:
    print(contar_bloques(n))
else:
    print("ERROR")