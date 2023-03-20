print("***COMO PREPARAR UN COLACAO***")

print("Nos dirigimos a la cocina")

print("*revisamos la despensa*")
print("Buscamos el colacao")
hay_colaco = (input("¿Habria colacao en la alacena? (Si/No)"))
if hay_colaco == "Si":
    print("sacamos el colacao")
if hay_colaco == "No":
    print("Que no, tienes compra")

print("*buscamos la leche*")

hay_leche = (input("¿Hay leche en la nevera? (Si/No)"))
if hay_leche == "Si":
    print("*sacamos la leche*")
if hay_leche == "No":
    print("No hay leche pringao")

if hay_leche == "No" or hay_colaco == "No":
    print("vales pura verga, ve a comprar al super..")

if hay_colaco == "No":
    print("Compras colacao")

if hay_leche == "No":
    print("Compras leche")

if hay_leche and hay_colaco == "Si":
    print("Busquemos un vaso para preparalo")

print("Ahora si viene lo chido")

vaso_colaco = input("Ya tienes el vaso listo? (Si/No)")

if vaso_colaco == "Si":
    print("Agrega el colacao al vaso")
    print("despues agrega la leche y ve buscando una cuchara")
    print("Ya con la cuchara en la mano, revuelve tu colacao hasta que se integre bien a la leche")
    print("ya todo integrado y rico disfruta")

if vaso_colaco != "Si":
    print("Espabila como no vas a tener un vaso en casa?")
    print("Largate antes que te pele")