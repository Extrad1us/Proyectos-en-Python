'''
Fundamentos de Programación Imperativa (Grupo 50)
Nombre y código del autor                           
                           :(2360308-2724) Alvarez Grajales Juan Jose
                           :(2360181-2724) Arango Marin Luis Angel
                           :() 
Fecha de realización: 20/04/2023
'''
import random
#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================

#Por cada función auxiliar y según el diseño realizado transcriba.


# Proposito: Determinar si un numero de 3 digitos tiene sus digitos iguales o diferentes
# Contrato: det_number(real)
# Ejemplo:
# Encabezado
# Cuerpo
def det_number (ran_number:int,):
    ram = ""
    if ran_number > (99) and ran_number < (999):
        if ran_number != 111 or ran_number != 222 or ran_number != 333 or ran_number != 444 or ran_number != 555 or ran_number != 666 or ran_number != 777 or ran_number != 888 or ran_number != 999:
            ram = ("Su numero tiene los digitos diferentes por lo tanto es *Verdadero*")
        else:
           ram =  ("Su numero tiene los digitos iguales por lo tanto es *Falso*")
    else:
        ram = ("El valoder debe de ser de 3 digitos")
    return(ram)


#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito: 
# Contrato: 
# Ejemplo: 
# Encabezado:
# Cuerpo
def principal ():
    ran_number = random.randint(99,999)
    confirm = det_number(ran_number)
    com = det_number(ran_number)
    resultado = print ("Su numero fue:",ran_number, com)
    return()
    

#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()




