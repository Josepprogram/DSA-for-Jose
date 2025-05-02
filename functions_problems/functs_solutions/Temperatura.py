#Se te proporciona una temperatura en grados Celsius. 
#Tu tarea es crear una funcion que pueda convertirla a grados Fahrenheit 
#y mostrar el resultado.

print("Este sistema calcula los grados celcius a Fahrenheit")
print("Por favor ingrese los grados celsius que desea calcular")
calc= float(input())

resultado= (calc * 9/5)+32

print(f"{resultado} grados Fahrenheit")