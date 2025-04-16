hemisferio = input("Hemisferio en el que se encuentra: ")
mes = input("Mes: ")
dia = int(input("Dia: "))
if hemisferio.lower() == "norte" :
    match mes.lower():
        case 'enero' :
            print("Invierno")
        case 'febrero' :
            print("Invierno")
        case 'marzo' :
            if dia <= 20 :
                print("Invierno")
            else :
                print("Primavera")
        case 'abril' :
            print("Primavera")
        case 'mayo' :
            print("Primavera")
        case 'junio' :
            if dia <= 20 :
                print("Primavera")
            else :
                print("Verano")
        case 'julio' :
            print("Verano")
        case 'agosto' :
            print("Verano")
        case 'septiembre' :
            if dia <= 20 :
                print("Verano")
            else :
                print("Otoño")
        case 'octubre' :
            print("Otoño")
        case 'noviembre' :
            print("Otoño")
        case 'diciembre' :
            if dia <= 20 :
                print("Otoño")
            else :
                print("Invierno")
        case _ :
            print("Mes ingresado incorrectamente")

elif hemisferio.lower() == "sur" : 
       match mes.lower():
        case 'enero':
            print("Verano")
        case 'febrero':
            print("Verano")
        case 'marzo' :
            if dia <= 20 :
                print("Verano")
            else :
                print("Otoño")
        case 'abril' :
            print("Otoño")
        case 'mayo' :
            print("Otoño")
        case 'junio' :
            if dia <= 20 :
                print("Otoño")
            else :
                print("Invierno")
        case 'julio' :
            print("Invierno")
        case 'agosto' :
            print("Invierno")
        case 'septiembre' :
            if dia <= 20 :
                print("Invierno")
            else :
                print("Primavera")
        case 'octubre' :
            print("Primavera")
        case 'noviembre' :
            print("Primavera")
        case 'diciembre' :
            if dia <= 20 :
                print("Primavera")
            else :
                print("Verano")
        case _ :
            print("Mes ingresado incorrectamente")
else :
    print("Ha ingresado incorrectamente lo pedido, vuelva a intentarlo.")