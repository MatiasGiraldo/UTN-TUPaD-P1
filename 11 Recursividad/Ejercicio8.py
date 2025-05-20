def contar_dig(num,dig):
    if num == 0:
        return 0
    else:
        ult_dig = num % 10
        rest_num = num // 10
        if ult_dig == dig:
            return 1 + contar_dig(rest_num,dig)
        else:
            return contar_dig(rest_num,dig)

num=int(input("Ingrese el numero a evaluar: "))
dig=int(input("Ingrese el digito que desee saber que se repita: "))
print(contar_dig(num,dig))