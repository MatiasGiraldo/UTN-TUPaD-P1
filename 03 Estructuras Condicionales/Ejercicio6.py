from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = int(mode(numeros_aleatorios))
mediana = int(median(numeros_aleatorios))
media = int(mean(numeros_aleatorios))
print(f"De la lista de numero aleatorios, su moda es {moda}, su mediana es {mediana} y su media es {media} ")
if moda < mediana < media : 
    print("Sesgo positivo")
elif media < mediana < moda :
    print("Sesgo negativo")
elif media == mediana == moda :
    print("Sin sesgo")