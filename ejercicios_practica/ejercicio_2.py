# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas

print("juegos con palabras \n")

texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:

    print('{} es mayor que {}'.format(texto_1, texto_2))

elif texto_2 > texto_1:

    print('{} es mayor que {}'.format(texto_2, texto_1))

else:

    print('{} es igual que {}'.format(texto_1, texto_2))

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):

    print('{} es mayor que {}'.format(texto_1, texto_2))

elif len(texto_1) < len(texto_2):

    print('{} es mayor que {}'.format(texto_2, texto_1))

else:

    print('{} tiene las mismas cantidad de letras que {}'.format(texto_1, texto_2))


# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[1] > texto_2[1]:
    
    print('{} su primera letra es mayor que la de la palabra {}'.format(texto_1, texto_2))
    print(texto_2[0])
    print(texto_2[1])
elif texto_2[1] > texto_1[1]:
    
    print('{} su primera letra es mayor que la de la palabra {}'.format(texto_2, texto_1))

else:
    
    print('la palabra {} tienen igual primera letra que {}'.format(texto_1, texto_2))


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda


if copia_texto_1 == texto_1:

    print('La palabra copia_texto_1({}) es igual que {}'.format(copia_texto_1, texto_1))

else:

    print('La palabra copia_texto_1({}) es distinta que {}'.format(copia_texto_1, texto_1))


# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:

    print('La palabra copia_texto_1({}) es distinta que {}'.format(copia_texto_1, texto_2))

else:

    print('La palabra copia_texto_1({}) es igual que {}'.format(copia_texto_1, texto_2))


print("Fin del Programa")
