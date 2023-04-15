'''
Fundamentos de Programación Imperativa (Grupo 50)
Nombre y código del autor                           
                           :(2360308-2724) Alvarez Grajales Juan Jose
                           :(2360181-2724) Arango Marin Luis Angel
                           :(2360170-2724) Herrera Rios Ivan David
Fecha de realización: 04/04/2023

'''
#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
# Proposito: Hallar la masa del usuario
# Contrato: masa (float, float)->float
# Ejemplo: masa(100,9.8)--> 10.20
# Encabezado def masa
# Cuerpo: 
def masap (PESOENT:float):
    masa = PESOENT/9.8
    return masa 

print (masap)
#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
# Proposito: Hallar el peso del usuario usando los datos digitados
# Contrato: peso_en_celestes (float, float, float)-->float
# Ejemplo: Se busca hallar el peso de una persona con masa de 10.20 en Marte, Se espera un resultado de 37.85 kg
# Encabezado def peso_en_celestes(gm, gl, gmo)
# Cuerpo:
def peso_en_celestes (masa:float):
    peso_mars = masa*3.711
    peso_luppiter = masa*24.79
    peso_moon = masa*1.622
    return (peso_mars, peso_luppiter, peso_moon)

#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito: Mostrar al usuario su peso en los diferentes cuerpos celestes
# Contrato: print_pesos ()
# Ejemplo: PESOENT = (100) --> (37.852199999999996, 252.85799999999998, 16.5444)
# Encabezado def print_pesos ()
# Cuerpo
def print_pesos ():
    PESOENT=float(input("Ingrese su peso en kilogramos"))
    masa=masap(PESOENT)
    pcelestes = peso_en_celestes(masa)
    print ("Pesas en marte, en jupiter y la luna")
    print (pcelestes)

#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================

print_pesos()