def validar(message):
    while True:
        try:
            data = float(input("Coloca "+message))
            return data
        except ValueError:
            print("El dato debe ser entero o decimal")


largo = validar("largo en metros: ")
ancho= validar("ancho en metros: ")
m2_x_caja = validar("metros cuadramos por caja: ")
precio_x_m2 = validar("precio por metro cuadrado: ")
precio_x_caja = m2_x_caja * precio_x_m2
m2_cuarto = largo * ancho
cajas = m2_cuarto / m2_x_caja
precio_total = cajas * precio_x_caja
print("Total de cajas que se necesitan ", cajas)
print("Precio total ", precio_total)