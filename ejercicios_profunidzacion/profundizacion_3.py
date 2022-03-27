# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

'''
while True:  
        
    try:
            
        temperatura_1 = float(input("Ingrese el primer valor de temperatura: "))

        temperatura_2 = float(input("ingrese el segundo valor de temperatura: "))

        temperatura_3 = float(input("Ingrese el tercer valor de temperatura: "))

        break

    except ValueError:

        print("Error, por favor intentalo de nuevo\n")'''

def evalua_temperatura():

    if temperatura_1 == temperatura_2 and temperatura_2 == temperatura_3:

        print("Las tres temperaturas son iguales")

#analizis de la temperatura maxima

    elif temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:

        print("La temperatura uno que es {} es la mayor".format(temperatura_1))
    
    elif temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:

        print("La temperatura dos que es ", temperatura_2, " es la mayor")

    elif temperatura_3 > temperatura_1 and temperatura_3 > temperatura_2:

        print("La temperatura tres que es ", temperatura_3, " es la mayor")

    elif temperatura_1 > temperatura_2 and temperatura_1 == temperatura_3:

        print("La temperatura uno y la tres son las mayores")
    
    elif temperatura_2 > temperatura_1 and temperatura_2 == temperatura_3:

        print("La temperatura dos y la tres son las mayores")

    elif temperatura_1 > temperatura_3 and temperatura_1 == temperatura_2:

        print("La temperatura uno y la dos son las mayores")


#analizis de la temperatura minima


    if temperatura_1 < temperatura_2 and temperatura_1 < temperatura_3:

        print("La temperatura uno que es ", temperatura_1, " es la menor")
    
    elif temperatura_2 < temperatura_1 and temperatura_2 < temperatura_3:

        print("La temperatura dos que es ", temperatura_2, " es la menor")

    elif temperatura_3 < temperatura_1 and temperatura_3 < temperatura_2:

        print("La temperatura tres que es ", temperatura_3, " es la menor")

    elif temperatura_1 < temperatura_2 and temperatura_1 == temperatura_3:

        print("La temperatura uno y la tres son las menores")
    
    elif temperatura_2 < temperatura_1 and temperatura_2 == temperatura_3:

        print("La temperatura dos y la tres son las menores")

    elif temperatura_1 < temperatura_3 and temperatura_1 == temperatura_2:

        print("La temperatura uno y la dos son las menores")


#promedio entre las temperaturas

    promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3

    print("El promedio de las tres temperaturas es:", promedio) 


try:
            
    temperatura_1 = float(input("Ingrese el primer valor de temperatura: "))

    temperatura_2 = float(input("ingrese el segundo valor de temperatura: "))

    temperatura_3 = float(input("Ingrese el tercer valor de temperatura: "))

    evalua_temperatura()

except ValueError:

   print("Error, no se ingreso un dato correcto\n")


print("Fin del programa")