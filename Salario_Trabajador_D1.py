''' Fundamentos de Programación Imperativa
Nombre y código del autor: Luis Angel Arango Marin (2360181-2724)
Fecha de realización: 21/03/2023'''


print("***PAGO DE NOMINA POR HORAS LABORADAS***") #TITULO DEL PROYECTO
#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
'''Por cada función auxiliar y según el diseño realizado transcriba.'''
# Proposito: Hallar el valor final que devengaria un empleado de tiendas D1
# Contrato: horas_laboradas*valorxhora = sueldo_final

##Ejemplo 1## valorxhora "30000"*horas_laboradas "35": debe de arrojar un salario de 1.050.000
VALORXHORA = 30000
horas_laboradas = 35
sueldo_final =  float(VALORXHORA * horas_laboradas )
print ("El sueldo final a devengar es de: ", sueldo_final, "ejemplo 1")

##Ejemplo 2## valorxhora "30000" * horas_laboradas "45": debe de arrojar un salario de 1350000
VALORXHORA = 30000
horas_laboradas = 45
sueldo_final =  float(VALORXHORA * horas_laboradas )
print ("El sueldo final a devengar es de: ", sueldo_final, "ejemplo 2")




#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito: Registrar la entrada de un dato numerico real el
#            cual equivale a una cantidad de horas laboradas por
#            un empleado del D1, para encontrar el sueldo final que
#            devengara.
# Contrato: valorxhora * horas_laboradas = sueldo_final.
# Ejemplo:

VALORXHORA = 30000 #Valor definido por el enunciado
horas_laboradas = float(input("Ingresa las horas laboradas: ")) # variable que encierra la entrada suministrada
if horas_laboradas < 65 :
    print ("Los datos deben de estar entre 20 y 65")
    StopIteration
if horas_laboradas > 20:
    print ("Los datos deben de estar entre 20 y 65")
    StopIteration
sueldo_final =  float(VALORXHORA * horas_laboradas ) # definicion que opera a las variables ya definidas
print ("El sueldo final a devengar es de: ", sueldo_final) # Llamado a la variable que muestra el resultado que buscamos
 
# Encabezado
# Cuerpo



            

#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================

