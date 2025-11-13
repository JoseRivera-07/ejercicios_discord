#Creamos una funcion para cambiar la edad ingresada por input a un numero y si no ingresa numeros que imprima que lo haga
def enteros():
    while True:
        edad = (input())
        try: 
            edad = int(edad)
            return edad
        except ValueError:
            print("Ups, hubo un error, ingresa nuevamente tu edad en digitos por favor")

#Utilizaremos una funcion que nos evalue si la licencia esta vigente y es compatible

def verificar_edad(edad_usuario, ed_min, ed_max):
    #Inicializamos desde ahora la edad permitida como false para controlar nuestro sistema
    ed_permitida = False

    #Verificamos que la edad se cumpla
    if (edad_usuario < ed_min) or (edad_usuario > ed_max):
        ed_permitida = False
    elif (edad_usuario >= ed_min) or (edad_usuario <= ed_max):
        ed_permitida = True
        

    return ed_permitida               

def verificar_licencia():

    licencia_vigente = False

    validar_l = input("Tienes licencia de conduccion (y/n): ")

    while True:
        match validar_l:
            case "y":
                licencia_vigente = True
                break
            case "n":
                licencia_vigente = False
                break
            case _:
                print("opcion invalida")    
    
    return licencia_vigente

def verify(name):
    while True: 
        tipo_v = input(f"{name}, vas a participar con: "
                               "1. Vehiculo propio "
                               "2. Vehículo prestado: ")   
                
        if tipo_v == "1":
            placa = input("Digita la placa de tu vehiculo tal cual aparece en la tarjeta de propiedad: ")
            v_propios.append(placa)
            print("Registro exitoso, cerrando app...")
            break
        elif tipo_v == "2":
            placa = input("Digita la placa del vehiculo que vas a utilizar: ")
            for vehiculo in v_autorizados:
                if vehiculo == placa:
                    print("El vehiculo esta autorizado, Registro exitoso")
                    break
                else: 
                    print("El vehiculo no ha sido autorizado, cerrando app...")
                    break
            break
        else: 
            print("Opcion invalida")


#Damos bienvenida al usuario con un print y posterior a eso solicitamos la entrada de edad
print("----- Bienvenido al Registro de corredor -----")
print("")
print("Para continuar, queremos que nos cuentes algo, ¿Cuantos años tienes?: ")

#Llamamos a una funcion que nos haga el cambio de tipo de dato y nos verifique que tipo de dato ingresamos por consola
edad_usuario = enteros()#Capturamos la edad en una variable para luego usarla
#Implementamos desde ahora una edad minima para participar, como tambien una máxima
edad_minima = 18
edad_máxima = 60

#Implementamos una lista de vehiculos autorizados
v_autorizados = ["RFY 90E", "ASD 123"]
v_propios = []

#Llamamos a la funcion edad para validar que cumpla el requisito
val_edad = verificar_edad(edad_usuario, edad_minima, edad_máxima) #Capturamos para luego usar

registrar = True

match val_edad:
    case True:
        name = input("Cuentanos como te llamas?: ")
        val_licencia = verificar_licencia() #capturamos tambien este resultado

        match val_licencia:
            case True:
                verify(name)
            case False:
                print(f"{name}, Registro fallido, No cumples el requisito de licencia, cerrando app...")
    
    case False:
        print("Registro fallido, No cumples con la edad, cerrando app...")