def segundos_a_horas(seg):
    return seg/3600
seg = int(input("Ingrese cantidad de segundos: "))
horas = segundos_a_horas(seg)
print(f"Los segundos ingresados equivalen a {horas} hora/s")