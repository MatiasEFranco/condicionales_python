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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

texto_1 = str(input("Por favor ingrese la primera palabra: "))

texto_2 = str(input("Por favor ingrese la segunda palabra: "))

texto_3 = str(input("Por favor ingrese la tercer palabra: "))

longitud_1 = len(texto_1)

longitud_2 = len(texto_2)

longitud_3 = len(texto_3)

print('''Que desea realiza
Coloque un 1 si deasea Ordenar por orden alfabético 
Coloque un 2 si deasea Ordenar por cantidad de letras ''')

comando = str(input())  #guardo en la variable el valor ingresado por el usuario para verificar que accion desea realizar
                        #lo guardo como string para poder salvar el programa si el ususario ingresa una letra en vez de un número

if comando == "1":
    
    if texto_1 == texto_2 and texto_1 == texto_3:

        print("Las tres palabras son iguales")
    
    elif texto_1 > texto_2 and texto_1 > texto_3:

        if texto_2 > texto_3:

            print("La palabra mayor es ", texto_1, " luego le sigue ", texto_2, " y luego ", texto_3)

        else:

            print("La palabra mayor es ", texto_1, " luego le sigue ", texto_3, " y luego ", texto_2)

    elif texto_2 > texto_1 and texto_2 > texto_3:

        if texto_1 > texto_3:

             print("La palabra mayor es ", texto_2, " luego le sigue ", texto_1, " y luego ", texto_3)

        else:

            print("La palabra mayor es ", texto_2, " luego le sigue ", texto_3, " y luego ", texto_1)

    elif texto_3 > texto_1 and texto_3 > texto_2:

        if texto_1 > texto_2:

             print("La palabra mayor es ", texto_3, " luego le sigue ", texto_1, " y luego ", texto_2)

        else:

            print("La palabra mayor es ", texto_3, " luego le sigue ", texto_2, " y luego ", texto_1)

    elif texto_1 == texto_2 and texto_1 > texto_3:

        print("La palabra mayor es ", texto_1)

    elif texto_1 == texto_2 and texto_3 > texto_1:

        print("La palabra mayor es ", texto_3)
        
    elif texto_1 == texto_3 and texto_1 > texto_2:

        print("La palabra mayor es ", texto_1)

    elif texto_1 == texto_3 and texto_2 > texto_1:

        print("La palabra mayor es ", texto_2)


    elif texto_2 == texto_3 and texto_2 > texto_1:

        print("La palabra mayor es ", texto_2)

    elif texto_2 == texto_3 and texto_1 > texto_2:

        print("La palabra mayor es ", texto_1)

elif comando == "2":

    if longitud_1 == longitud_2 and longitud_1 == longitud_3:

        print("Las tres palabras son iguales")
    
    elif longitud_1 > longitud_2 and longitud_1 > longitud_3:

        if longitud_2 > longitud_3:

            print("La palabra mayor es ", texto_1, " luego le sigue ", texto_2, " y luego ", texto_3)

        else:

            print("La palabra mayor es ", texto_1, " luego le sigue ", texto_3, " y luego ", texto_2)

    elif longitud_2 > longitud_1 and longitud_2 > longitud_3:

        if longitud_1 > longitud_3:

             print("La palabra mayor es ", texto_2, " luego le sigue ", texto_1, " y luego ", texto_3)

        else:

            print("La palabra mayor es ", texto_2, " luego le sigue ", texto_3, " y luego ", texto_1)

    elif longitud_3 > longitud_1 and longitud_3 > longitud_2:

        if longitud_1 > longitud_2:

             print("La palabra mayor es ", texto_3, " luego le sigue ", texto_1, " y luego ", texto_2)

        else:

            print("La palabra mayor es ", texto_3, " luego le sigue ", texto_2, " y luego ", texto_1)

    elif longitud_1 == longitud_2 and longitud_1 > longitud_3:

        print("La palabra mayor es ", texto_1)

    elif longitud_1 == longitud_2 and longitud_3 > longitud_1:

        print("La palabra mayor es ", texto_3)
        
    elif longitud_1 == longitud_3 and longitud_1 > longitud_2:

        print("La palabra mayor es ", texto_1)

    elif longitud_1 == longitud_3 and longitud_2 > longitud_1:

        print("La palabra mayor es ", texto_2)


    elif longitud_2 == longitud_3 and longitud_2 > longitud_1:

        print("La palabra mayor es ", texto_2)

    elif longitud_2 == longitud_3 and longitud_1 > longitud_2:

        print("La palabra mayor es ", texto_1)

else:

    print("Error, no se ingreso un valor correcto")


print("Fin del Programa")