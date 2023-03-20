print("****DESCUENTO EN LA ENTRADA DEL PEDREGAL****")

edad= (int(input("Edad del usuario: ")))
carnet_benf = (input("Que tipo de beneficiaro es? (U: Universitario, F: Familia afiliada, M: Menor de edad, V: VIP: "))

if (edad < 35 and edad > 25 and carnet_benf == "U") or edad < 10 or carnet_benf == "V" or carnet_benf == "F":
    print("aplica para el descuento del 25%")

else:
    print("No aplicas para el descuento")