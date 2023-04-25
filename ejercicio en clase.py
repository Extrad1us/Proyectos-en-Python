#proposito: Determinar los dias segun que mes sea
#Contrato: diasmes (text) --> entero
#Ejemplo: "Enero"--> 31
def diasmes (mes):
    dias = 28
    if mes == "Enero" or "Mayo" or "Agosto" or "Octubre" or "Diciembre":
        dias = 31
    else:
         if mes == "Abril" or "Junio" or "Septiembre" or "Noviembre":
             dias = 30
    return ()



def principal ():
    mes = str(input("Ingrese el mes: "))
    d = diasmes(dias)
    print ("El mes de ",mes,"tienes ", d ,"dias")
    return()

principal ()
