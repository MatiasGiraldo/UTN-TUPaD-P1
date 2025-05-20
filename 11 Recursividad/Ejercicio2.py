def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-2) + fibonacci(pos-1)

pos= int(input("Ingrese la posicion hasta que se mostrará: "))
for i in range(0,pos+1):
    print(f"Posicion {i}: {fibonacci(i)}")