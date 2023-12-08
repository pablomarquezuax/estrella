import turtle

# Creamos una fución con un bucle para que se haga la estrella
def dibujar_estrella(size):
    for _ in range(9):
        turtle.forward(size)
        turtle.right(160)
# "size" es una variable que puede ser cambiada y decide el tamaño de la estrella
# "range" es el numero de veces que se repite la acción del bucle, por tanto, el número de puntas de la estrella
# 160 es el angulo de giro que realiza la flecha para hacer la siguiente punta


# Características del dibujo
turtle.speed(4)  # Para ajustar la velocidad a la que se dibuja la estrella
turtle.pensize(2) # Para ajustar el grosor de las lineas del dibujo
turtle.pencolor("black") # para ajustar el color del dibujo


# Dibujar la estrella
dibujar_estrella(300)  
# Aqui se puede cambiar el valor de la variable size para cambiar el tamaño de la estrella



# Para que la ventana no se cierre cuando se termine de dibujar la estrella
turtle.done()
