
"""Programa para hacer calculos financieros
1) Interes simple
2) Interes compuesto
3) Ecuaciones de valores equivalentes
4) Tasa efectiva
5) Tasas equivalentes
6) Anualidades simple ordinarias
7) Anualidades anticipadas simples
8) Tablas de amortizacion
9) Fondos de amortizacion
10) Salir

"""

i = True
ii = True
Si = True
No = False






#InteresSimple
def InteresSimple():
    print "Puedes calcular monto, capital y el interes"
    while i == True:
        operacion == input ("\nCual quieres calcular? \n1)Monto \n2)Capital \n3)Interes\n")

        if operacion == 1:
           capital = input("Ingresa el valor del capital\n")
           tiempo = input("Elige el tiempo en: \n1)Dias \n2)Semanas \n3)Meses\n4)anos\n")

           if tiempo == 1:
               CantidadTiempo = input("Ingresa la cantidad de dias:\n")
           elif tiempo == 2:
               CantidadTiempo = input("Ingresa la cantidad de semanas:\n")
           elif tiempo ==3:
               CantidadTiempo = input("Ingresa la cantidad de meses:\n")
           elif tiempo == 4:
               CantidadTiempo = input("Ingresa la cantidad de anos:\n")
           else:


            interes = input ("Ingresa el valor de la tasa de interes\n")
        capitalizacion = input ("Cada cuanto es capitalizable: \n1)Dias \n2)Semanas \n3)Meses\n4)anos\n")
        if capitalizacion == 1:
               CantidadTiempo = input("\nIngresa la cantidad de dias")
        elif capitalizacion == 2:
               CantidadTiempo = input("\nIngresa la cantidad de semanas:\n")
        elif capitalizacion ==3:
               CantidadTiempo = input("Ingresa la cantidad de meses")
        elif capitalizacion == 4:
               CantidadTiempo = input("Ingresa la cantidad de anos")

               #



print "\n*********Programa para hacer calculos financieros*********\n"

while i == True:

    operacion = input("Elige la operacion que deseas hacer: \n1) Interes simple  \n2) Interes compuesto \n3) Ecuaciones de valores equivalentes \n4) Tasa efectiva \n5) Tasas equivalentes \n6) Anualidades simples ordinarias \n7) Anualidades anticipadas simples \n8) Tablas de amortizacion \n9) Fondos de amortizacion \n10) Salir\n ")

    if operacion == 1:
        InteresSimple()

    else:
        print "Ingresa una opcion valida"

    i = input("\nQuieres hacer otra operacion? \nSi \nNo\n ")







