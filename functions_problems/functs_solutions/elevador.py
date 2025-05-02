#Debes crear una funcion que calcule las veces que debe subir el ascensor.
#Los parametros de la funcion son n (el número total de personas) 
#y capacidad (el número máximo de personas que el ascensor puede transportar simultáneamente). 
#Todas las personas quieren ir de la planta baja a la superior.
# Tu tarea es calcular el número de vueltas que debe dar el ascensor para transportar a todas las personas a la planta superior.

print("Coloque la cantidad de personas que estan esperando el ascensor")
n = int(input())
print("Dicte la capacidad de personas que puede llevar el ascensor")
capacidad = int(input())
cont = 0

while n != 0:

    if n >= capacidad and n != 0:
        n = n-capacidad
        cont=cont+1
    if n < capacidad and n > 0:
        cont=cont+1
        n = n-capacidad
    if n <= 0:
        break

print(f"La cantidad de vueltas que dara el ascensor para llevar a todas la personas hasta su destino es: {cont}")    
