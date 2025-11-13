#Creamos una funcion que nos evalue el nombre
def banned(name, users): #Le entregamos el parametro del nombre del usuario
 
    for user in users:#Recorremos la lista de usuarios restringidos
        if user == name: #Validamos si la condicion se cumple (Si el usuario esta en la lista)
            print("Invalid user, you are BANNED, close the system...") #Imprimimos porque no puede ingresar
            break
        else:
            return True
        
    

#Ahora creamos la funcion que nos va a revisar el codigo que ingrese el usuario para validar si cumple los criterios
def v_code(code):
    code = int(code)
    last = code % 10

    if last == 7:
        access = True
        return access
    elif code % 2 == 0: 
        access = True
        return access
    else:
        access = False
        return access
    
    
#Ahora bien, vamos a crear una lista con nombres restringidos
users = ["joselito","samuelano", "veronica", "quinto" ]

#Vamos a pedir al usuario que ingrese su nombre
print("------ Hello, and Welcome to Access control ------")
print("")
name = input("Dear user, what is your name?: ")

user_status = banned(name, users)

if (user_status == True):
    code = input("Enter an code: ")
    code_status = v_code(code)
    if (code_status == True):
        print("Welcome user")
    elif (code_status == False):
        print("Your code is not a multiple of 2 or  not ends with a digit 7, close the system...")