def es_palindromo(pal):
    if len(pal) < 2:
        return True
    elif pal[0] == pal[-1]:
        return es_palindromo(pal[1:-1])
    else:
        return False

pal= input("Ingrese palabra: ")
print(es_palindromo(pal))