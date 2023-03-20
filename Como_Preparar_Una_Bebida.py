print("***COMO PREPARAR UN MILO***")

print("Nos dirigimos a la cocina")

print("*revisamos la despensa*")
print("Buscamos el Milo")
hay_Milo = (input("¿Habria Milo en la alacena? (Si/No)"))
if hay_Milo == "Si":
    print("sacamos el colacao")
if hay_Milo == "No":
    print("Que no, tienes compra")

print("*buscamos la leche*")

hay_leche = (input("¿Hay leche en la nevera? (Si/No)"))
if hay_leche == "Si":
    print("*sacamos la leche*")
if hay_leche == "No":
    print("No hay leche pringao")

if hay_leche == "No" or hay_Milo == "No":
    print("vales pura verga, ve a comprar al super..")

if hay_Milo == "No":
    print("Compras Milo")

if hay_leche == "No":
    print("Compras leche")

if hay_leche and hay_Milo == "Si":
    print("Busquemos un vaso para preparalo")

print("Ahora si viene lo chido")

vaso_Milo = input("Ya tienes el vaso listo? (Si/No)")

if vaso_Milo == "Si":
    print("Agrega el Milo al vaso")
    print("despues agrega la leche y ve buscando una cuchara")
    print("Ya con la cuchara en la mano, revuelve tu Milo hasta que se integre bien a la leche")
    print("ya todo integrado y rico disfruta")

if vaso_Milo != "Si":
    print("Espabila como no vas a tener un vaso en casa?")
    print("Largate antes que te pele")