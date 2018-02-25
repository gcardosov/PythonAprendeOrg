#Funciones en python
"""print "Consta de:"
print "la palabra reservada def el nombre, las variables para el proceso y 2 puntos"
print "def funcion(argumentos):"""
#Calculo de areas
F = 3.141516
i = True
Si = True
No = False
#Area del cuadrado
def acuadrado():
    lado = input ("Cual es el valor del lado:\n")
    x = lado **2
    print"\nEl area del cuadrado es",x,"unidades cuadradas"

#Area del triangulo
def atriangulo():
    base = input ("Cual es el valor de la base:\n")
    altura = input("Cual es el valor de la altura:\n")
    y = (base*altura)/2
    print "\nEl area del triangulo es ",y," unidades cuadradas"

#Area del circulo
def acirculo ():
    radio = input("Cual es el valor del radio:\n")
    z = (F* radio)**2
    print "\nEl area del circulo es ",z, "unidaes cuadradas"

while i == True:
    area = input("\nElije la figura geometrica para calcular su area \nCuadrado=1 \nTriangulo=2 \nCirculo=3\n")

    if area == 1:
        acuadrado()

    elif area == 2:
        atriangulo()

    elif area == 3:
        acirculo()

    else:
        print "Ingresa una opcion valida"

    i = input("\nQuieres calcular el area de otra figura? \nSi \nNo\n ")



