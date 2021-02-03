lado = int(input('Ingresar la distancia de lado en cm: '))
base = int(input('Ingresar la distancia de la base en cm: '))
if lado == base:
    area = base * lado
    print('Como es un cuadrado, su área es ' + str(area))
else:
    perimetro = 2*base + 2*lado
    print('Como es un rectangulo, el perímetro es ' + str(perimetro))