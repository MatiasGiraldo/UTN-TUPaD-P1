original = {
    'Alemania': 'Berlin',
    'Chile': 'Santiago',
    'Ecuador': 'Quito',
    'Venezuela': 'Caracas',
    'España': 'Madrid'
}
print(original)

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print(invertido)