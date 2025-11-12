dias_entreno = input("Hola, cuantos dias entrenaste esta semana: (1-5): ")
dias_entreno = int(dias_entreno)
puntos = 0

if dias_entreno >= 4:
    puntos = puntos + 1
    print("¡Excelente disciplina")
    print("Has ganado 1 punto de energía, tu racha actual es: ", puntos) 
    
elif dias_entreno == 2 or 3:
    print("Bien pero puedes dar más")
elif dias_entreno == 0 or 1:
    print("No aflojes, tu puedes mejorar")
else:
    print("dato invalido")