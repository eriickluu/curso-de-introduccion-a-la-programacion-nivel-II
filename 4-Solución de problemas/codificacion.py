largo = float(input("Coloca el largo en metros: "))
ancho= float(input("Coloca el ancho en metros: "))
m2_x_caja = float(input("Coloca los metros cuadramos por caja: "))
precio_x_m2 = float(input("Coloca el precio por metro cuadrado: "))
precio_x_caja = m2_x_caja * precio_x_m2
m2_cuarto = largo * ancho
cajas = m2_cuarto / m2_x_caja
precio_total = cajas * precio_x_caja
print("Total de cajas que se necesitan ", cajas)
print("Precio total ", precio_total)