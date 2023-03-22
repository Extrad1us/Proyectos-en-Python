nombre = input("Ingresa tu nombre")
edad = int (input("Ingresa tu edad"))
estatura = float(input("Ingresa tu estatura"))

#Las comas importan en este tipo de conjunciones de texto y definiciones
print ( "hola", nombre, "tienes", edad, "años, y mides", estatura, "metros") 

if edad < 18 :
    print("eres mayor de edad")