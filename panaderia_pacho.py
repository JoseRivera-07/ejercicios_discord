precio_pan = 300

descuento1 = 0.1

descuento2 = 0.2

cantidad = input("Bienvenido a la panaderia de pacho, cuantos panes quiere comprar?: ")
cantidad = int(cantidad)

if cantidad > 20:
    print("Tu compra incluye un descuento especial!!!")

    sub_total = precio_pan * cantidad
    deduccion_descuento = sub_total * descuento1
    total = sub_total - deduccion_descuento
    print("El total de su compra es: ", total)
elif cantidad > 50:
    print("Tu compra incluye un descuento especial!!!")

    sub_total = precio_pan * cantidad
    deduccion_descuento = sub_total * descuento2
    total = sub_total - deduccion_descuento

    print("El total de su compra es: ", total)
elif 0 < cantidad >= 20:
    sub_total = precio_pan * cantidad

    print("Su compra no aplica al descuento que tiene la panaderia")
    print("El total de su compra es de: ", sub_total)
else:
    print("cantidad invalida")