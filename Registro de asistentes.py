#Definimos un stopper
cerrar = "FIN"

#Inicializamos la variable desicion pero la iniciamos vacia
desicion = ""

#Creamos una lista donde vamos a guardar los nombres ingresados
nombres = []

#Le damos una bienvenida al usuario
print("---- Bienvenido al Registro de asistentes -----")

cont = 1 #Este cont nos ayudará a darle un indice a cada persona que se ingrese

#Hacemos un bucle para poder ingresar varios nombres
while desicion != cerrar:
    nombre = input(f"Cual es el nombre de la {cont}° persona a ingresar?: ") 

    if nombre.strip() == "":
       print("Ingresó un usario vacio")
    else:
        nombre = nombre.capitalize() #Aqui convertimos la primera letra del nombre a mayuscula 
        nombres.append(nombre) 



    
    if (cont > 1): #Esto nos permite ingresar el primer nombre sin que aparezca la opcion salir siempre
        desicion = input("Deseas salir? Puedes escribir fin: ")
        print("")
        desicion = desicion.upper() #con upper convertimos lo ingresado a mayusculas
        if (desicion == cerrar):
            break #freno de mano del while
        else:
            print("No saliste del sistema, volveras a agregar persona")
            print("")
    else:
        pass #si la condicion no se cumple simplemente lo ignoramos y continuamos el codigo
    
    cont += 1 #Incrementamos en contador para que continue asignando indices a los users sucesivamente

#Vamos a mostar el total de nombres ingresados junto con los nombres ingresados
print(f"Se ingresaron {len(nombres)} nombres en el sistema")

#Con la siguiente funcion vamos a ver cuales son los nombres que se repiten
repetidos = set([nombre for nombre in nombres if nombres.count(nombre) > 1])
print("Nombres repetidos:", repetidos)

#Imprimimos los nombres ingresados y cerramos el sistema
print(f"Las personas ingresadas son: {nombres}, cerrando sistema... ")