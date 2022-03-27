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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

def comparar():
    
    '''while True:  #en este caso utilizo el "while True" junto con el "try except" por si el usuario se confunde e ingresa un valor que no sea numerico
        
        try:
            
            numero_1 = float(input("Ingrese el primer numero: "))

            numero_2 = float(input("ingrese el segundo numero: "))

            break

        except ValueError:

            print("Error, por favor intentalo de nuevo\n")'''

    resultado = numero_1 - numero_2

    if resultado < 0:

        print("El resultado de la resta es ", resultado, " y es negativo")

    elif resultado > 0:

        print("El resultado de la resta es ", resultado, " y es positivo")

    else:
        
        print("El resultado de la resta es ", resultado, " y es cero")



try:
    numero_1 = float(input("Ingrese el primer numero: "))

    numero_2 = float(input("ingrese el segundo numero: "))

    comparar()  #utilizo una funcion ya que me result amas practico poder llamarla en cualquier parte del programa y de esta manera no tengo que reescribir el codigo

except ValueError:

    print("Error, no se ingreso un dato correcto\n")


print("Fin del Programa")