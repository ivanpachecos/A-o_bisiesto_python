#Programa para ver si el año que ingreso es bisiesto o no

anio = int(input("Ingrese su nunero: "))

if (anio % 4 == 0 and anio % 100 !=0) or anio % 400 ==0:
  print(f"El año {anio}, es bisiesto")

else:
  print("No es bisiesto")

