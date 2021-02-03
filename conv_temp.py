def temp(cent):
    fehre = (int(cent) * 1.8) + 32
    print(cent + '° grados centígrados en grados fahrenheit es ' + str(fehre))

cent = input('Ingrese la temperatura en grado centígrados: ')
temp(cent)