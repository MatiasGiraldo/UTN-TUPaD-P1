frase = input("Ingrese frase o palabra: ")
ultimo = frase[-1].lower()
vocales = "aeiou"
if ultimo in vocales:
    print(frase + "!")
else :
    print(frase)
