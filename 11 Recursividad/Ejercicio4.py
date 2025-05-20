def num_ent_pos_dec(num):
    if num == 0:
        return ""
    else:
        return num_ent_pos_dec(num // 2) + str(num % 2)

num = int(input("Ingrese numero decimal: "))
if num < 0:
    print("ERROR, ha ingresado numero negativo")
elif num == 0:
    print("0")
else:
    binario = num_ent_pos_dec(num)
    print(f"El número {num} en binario es: {binario}")
