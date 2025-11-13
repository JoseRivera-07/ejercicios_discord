#Creamos una funcion para cambiar la edad ingresada por input a un numero y si no ingresa numeros que imprima que lo haga
def enteros():
    while True:
        edad = (input())
        try: 
            edad = int(edad)
            return edad
        except ValueError:
            print("Ups, hubo un error, ingresa nuevamente tu edad en digitos por favor")

#Damos bienvenida al usuario con un print y posterior a eso solicitamos la entrada de edad
print("----- Bienvenido al sistema Etapa vital -----")
print("")
print("Para continuar, queremos que nos cuentes algo, ¿Cuantos años tienes?: ")

#Llamamos a una funcion que nos haga el cambio de tipo de dato y nos verifique que tipo de dato ingresamos por consola
edad_usuario = enteros()#Capturamos la edad en una variable para luego usarla

#Creamos una lista donde guardaremos las diferentes etapas del usuario
etapa = ["Infante", "Estudiante escolar", "Universitario", "Adulto activo", "Adulto mayor jubilado"]

#Entramos a validar a que etapa pertenece segun su edad

if 0 < edad_usuario < 6:
    print("Segun tu edad, tu etapa vital es: ", etapa[0])
elif 6 <= edad_usuario <= 17:
    print("Segun tu edad, tu etapa vital es: ", etapa[1])
elif 18 <= edad_usuario <= 25:
    print("Segun tu edad, tu etapa vital es: ", etapa[2])
elif 25 < edad_usuario < 59:
    print("Segun tu edad, tu etapa vital es: ", etapa[3])
elif 60 < edad_usuario < 95:
    print("Segun tu edad, tu etapa vital es: ", etapa[4])
else:
    print("La edad que ingresaste no es valida (No determinado)")