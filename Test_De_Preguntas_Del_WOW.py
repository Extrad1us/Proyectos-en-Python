titulo = ("******Test World Of Warcraft******""\n")
print(titulo + "-" * len(titulo))

puntuacion = 0

pregunta_1 = input("1.	¿Cuál es el nombre del chaman que fue jefe de guerra de la horda?""\n")

if pregunta_1 == "Thrall":
    print("Respuesta correcta + 4 puntos")
    puntuacion = puntuacion + 4

if pregunta_1 != "Thrall":
    print("incorrecto + 0 puntos")
    puntuacion + 0

pregunta_2 = input("2.	¿La capital de la alianza se encuentra actualmente en?""\n")

if pregunta_2 == "Ventormenta":
    print("Respuesta correcta + 4 puntos")
    puntuacion = puntuacion + 4

if pregunta_2 != "Ventormenta":
    print("Incorrecto + 0 puntos")
    puntuacion + 0

pregunta_3 = input("3.	¿Cuál es el nombre del príncipe corrompido por la plaga que mato a su padre?""\n")

if pregunta_3 == "Arthas":
    print("Respuesta correcta + 4 puntos")
    puntuacion = puntuacion + 4
if pregunta_3 != "Arthas":
    print("Incorrecto + 0 puntos")
    puntuacion + 0

pregunta_4 = input("4.	¿El joven príncipe en que continente encontró el poder que lo llevo a su perdición?""\n")

if pregunta_4 == "Rasganorte":
    print("Respuesta correcta + 4 puntos")
    puntuacion = puntuacion + 4
if pregunta_4 != "Rasganorte":
    print("Incorrecto + 0 puntos")
    puntuacion + 0

pregunta_5 = input("5.	¿Cuál es la mejor clase melee del juego? ""\n")

if pregunta_5 == "Caballero de la muerte":
    print("Correcticimo + 20 puntos")
    puntuacion = puntuacion + 20
if pregunta_5 == "Picaro":
    print("mew + 10 puntos")
    puntuacion = puntuacion + 10
if pregunta_5 == "Guerrero":
    print("mew + 10 puntos")
    puntuacion = puntuacion + 10
if pregunta_5 == "Monje":
    print("God + 12 puntos")
    puntuacion = puntuacion + 12
if pregunta_5 == "Cazador de demonios":
    print("Re gay + 5 puntos")
    puntuacion = puntuacion + 5

print("Tu puntuacion es:")
print(puntuacion)

if puntuacion > 30 :
    print("\n""{} Puntos, Level experto".format(puntuacion))
elif puntuacion > 15 :
    print("\n""{} Puntos, Level medio".format(puntuacion))
else :
    print("\n""{} Puntos, Level noob".format(puntuacion))






