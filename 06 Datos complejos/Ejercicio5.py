frase = input("Ingrese frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
recuento = {}
for elemento in palabras:
    if elemento in recuento:
        recuento[elemento] += 1
    else:
        recuento[elemento] = 1
print(palabras_unicas)
print(f"Recuento: {recuento}")