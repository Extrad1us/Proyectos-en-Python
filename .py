import random

def selc_dep (ran_number:random):
    Vain = "Dato erroneo"
    if ran_number > 99 < 999 :
        if ran_number != 111 or 222 or 333 or 444 or 555 or 666 or 777 or 888 or 999:
            Vain = ("Tiene los digitos diferentes por lo cual es valido")
        else:
             Vain = ("Tiene los digitos iguales por lo cual es invalido")
    return()    

def principal ():
    ran_number = int(input("ingrese"))#random.randint(99, 999)
    alet = selc_dep(ran_number)
    print ("El numero",ran_number, alet)
     
    



principal()