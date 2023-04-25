'''
Autor: Luis Angel Arango Marin
Codigo: 2360181
'''
# Prueba de condicionales
#Proposito: determinar si una persona es mayor
#contrato: principal()
#Casos de ejemplo: edad: 18 --> usted es mayor

def principal ():
   edad = int(input("Digite su edad: "))
   m = determinar(edad)
   return ()

#Proposito: determinar si una persona es mayor
#Contrato: determinarMayor(int)-->texto
#caso de ejemplo: determinarMayor(18)--> Ustede es mayor
#caso de ejemplo: determinarMayor(15)--> Ustede es menor
def determinar (edad:int):
     if edad >= 18:
      resultado =("Usted es mayor de edad")
     else:
      resultado = ("Usted es menor")
     return (resultado)
    


principal ()

#proposito: Determinar los dias segun que mes sea
#Contrato: diasmes (text) --> entero
#Ejemplo: "Enero"--> 31
'''def diasmes (mes):
    dias = 28
    if mes == "Enero" or "Mayo" or "Agosto" or "Octubre" or "Diciembre":
        dias = 31
    else:
         if mes == "Abril" or "Junio" or "Septiembre" or "Noviembre":
             dias = 30
    return ()



def principal ():
    mes = str(input("Ingrese el mes: "))
    d = diasmes(mes)
    print ("El mes de ",mes,"tienes ", d,"dias")
    return()

principal ()'''

