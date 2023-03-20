titulo = "********CONVERSOR DE MONEDA********"
print("_" * len(titulo) + titulo + "_" * len(titulo))
euro = 1
comando = 0;
pesosceuro = 4468
pesoscdola = 4375
operacion = input("\nQue convercion deseas realizar: \n"
                  "1. Euros a P1esos\n"
                  "2. Pesos a Euros\n"
                  "3. Dolares a Pesos\n"
                  "4. Pesos a Dolares\n"
                  )


if operacion == "1":
    
    euros =  float(input("Que valor de euros deseas convertir?: \n"))
    print("convirtiendo €{} euros a pesos".format(euros))
    print("Nuevo saldo en pesos colombianos es de: ${} Pesos".format(euros*pesosceuro))
  

elif operacion == "2":
    pesos = float(input("Que valor de pesos desea convertir? \n"))
    print("Convirtiendo ${} pesos a euros".format(pesos))
    print("Nuevo saldo en Euros es de : €{} Euros".format(pesos/pesosceuro))

elif operacion == "3":
    dolares = float(input("Que valor de Dolares desea convertir? \n"))
    print("Convirtiendo ${} Dolares a Pesos".format(dolares))
    print("Nuevo saldo en Pesos es de: ${} Pesos".format(dolares*pesoscdola))

elif operacion == "4":
    pesosd = float(input("Que valor de Pesos desea convertir? \n"))
    print("Convirtiendo ${} Pesos a Dolares".format(pesosd))
    print("Nuevo saldo en Dolares es de: ${} Dolares".format(pesosd/pesoscdola))


      

    





