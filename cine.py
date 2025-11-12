tarifa1 = 0
tarifa2 = 5000
tarifa3 = 8000
tarifa4 = 4000

print("Bienvenido al cine, en el cine estrella tenemos grandes beneficios para ti: ")
print("Niños menores de 5 años entran gratis")
print("Niños entre 5 a 11 años entran por solo $",tarifa2)
print("Jovenes y adultos entre los 12 y 59 años entran con tarifa normal: $", tarifa3)
print("Adulto mayor (a partir de los 60 años) entran con una tarifa exclusiva: $",tarifa4)

edad = input("Ahora bien, cuentanos que edad tienes?: ")
edad = int(edad)

if 0 <= edad < 5:
    print("tu entada cuesta: $", tarifa1)
elif 5 <= edad <= 11:
    print("tu entada cuesta: $", tarifa2)
elif 11 < edad < 60:
    print("tu entada cuesta: $", tarifa3)
elif edad >= 60:
    print("tu entada cuesta: $", tarifa4)
else:
    print("Edad invalida")

