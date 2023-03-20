import random

print("***SALVA TU MUNDO ADIVINANDO***")
print("Tienes que adivinar un numero del 1 al 10 que hara que tu mundo no estalle")
numero_magico = int(input("Inserta tu numero del 1 al 10 que salvara la humanidad: "))
numero_salvador = random.randint(1, 10)

if numero_magico > 10:
    print("que es entre 1 y 10 tarado ")

if numero_magico < 1:
    print ("Enserio?")

if numero_magico != numero_salvador:
    print("Todos murieron por tu incapacidad, era el numero {} ".format(numero_salvador))

if numero_magico == numero_salvador:
    print("Joa hermano eres un heroe sin capa, el numero era {}".format(numero_salvador))
    
