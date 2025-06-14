def fact(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return fact(num-1) * num
num=int(input("Ingrese el valor hasta donde mostrar: "))
for i in range (1,num+1):
    print(fact(i))