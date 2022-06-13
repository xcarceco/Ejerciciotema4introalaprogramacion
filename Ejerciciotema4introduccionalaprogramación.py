# En este ejercicio practicarás las estructuras de control, para ello deberás crear:
# Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
# Pista: Los números inferiores a 0 son negativos y los superiores, positivos.



numeroIf=int(input('introduce un numero:',))
estacion=input('Que estación es:',)
numeroIf2=numeroIf-(numeroIf-3)
numeroIf3=0
print(numeroIf)
# Crea un bucle While, este bucle tendrá que tener como condición que la variable
# numero While sea inferior a 3, el bloque de código que tendrá el bucle deberá:
# Incrementar el valor de la variable en uno cada vez que se ejecute.
# Mostrarlo por pantalla cada vez que se ejecute.
# Para el bucle Do While, deberás crear la misma estructura que en el While,
# pero solo se debe ejecutar una vez.

if numeroIf>0:
    print('es positivo')
elif numeroIf<0:
    print('es negativo')
elif numeroIf==0:
    print('es 0')
while numeroIf<3:
    numeroIf+=1
    print(numeroIf)
while numeroIf<3:
    print(numeroIf2)
    break
# Para el bucle For, crea una variable numero For, esta variable tendrá como valor
# 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su
# valor cada vez que se ejecute y deberá mostrarse por pantalla.
if numeroIf3<=0:
    numeroIf3+=1
    print('numeroIf3 es 0 y le sumamos 1:', numeroIf3)

#Por último, para el Switch, deberás crear la variable estacion,
# y distintos case para las cuatro estaciones del año. Dependiendo del valor de la
# variable estacion se deberá mandar un mensaje por consola informando de la estación
# en la que está. También habrá que poner un default para cuando el valor de la variable
# no sea una estación.

