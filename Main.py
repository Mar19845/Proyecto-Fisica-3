#JuanMarroquin 19845
print("Hola")
print('''Bienvenido
Al programa que resuelve ecuaciones diferenciales ''')

cat=''
while cat!='asdasdasf':
    try:
        cat=input('''
1. Ingresar Valores para graficar 
2. Fin de programa
Ingrese la opcion que desea usar:  ''')
    except:
        print("Ingrese un valor Valido")
        cat=input('''
1. Ingresar Valores para graficar 
2. Fin de programa
Ingrese la opcion que desea usar:  ''')
    if cat=='2':
        print("")
        print("Gracias por hacer uso del programa")
        break
    if cat=='1':
        #ingreso de los valores de la velociadad inicial
        print("Ingrese los valores de la VELOCIDAD INICIAL")
        while True:
            try:
                VelMagnitud = float(input("Ingrese la MAGNITUD de la VELOCIDAD: "))
                break
            except:
                print("Ingrese Un valor Valido")
        while True:
            try:
                VelDir = float(input("Ingrese la DIRRECCION de la VELOCIDAD: "))
                break
            except:
                print("Ingrese Un valor Valido")
        #ingreso de los valores del campo electrico
        print("Ingrese los valores del CAMPO ELECTRICO")
        #magnitud del campo
        while True:
            try:
                CampoMagnitud = float(input("Ingrese la MAGNITUD del CAMPO ELECTRICO: "))
                break
            except:
                print("Ingrese Un valor Valido")
        #sentido del campo
        while True:
            try:
                CampoSentido = float(input("Ingrese el SENTIDO del CAMPO ELECTRICO: "))
                break
            except:
                print("Ingrese Un valor Valido")
        #largo del campo
        while True:
            try:
                CampoLargo = float(input("Ingrese el LARGO del CAMPO ELECTRICO: "))
                break
            except:
                print("Ingrese Un valor Valido")
        #ancho del campo
        while True:
            try:
                CampoAncho = float(input("Ingrese el ANCHO del CAMPO ELECTRICO: "))
                break
            except:
                print("Ingrese Un valor Valido")
        #tipo de particula
        print("Ingrese los valores de la PARTICULA")
        while True:
            try:
                ParticulaTipo = float(input("Ingrese la PARTICULA que desea usar: "))
                break
            except:
                print("Ingrese Un valor Valido")
         while True:
            try:
                ParticulaCantidad = int(input("Ingrese el NUMERO DE PARTIULAS que desea usar: "))
                break
            except:
                print("Ingrese Un valor Valido")
        
        #333333333333333
        print(ParticulaCantidad)
    