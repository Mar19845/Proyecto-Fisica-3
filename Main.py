#JuanMarroquin 19845
#Carlos Raxtum 19721


# Cargas a utilizar
C_neutra = 0
C_positiva = 1.6e-19
C_negativa = -1.6e-19
C_alfa = 3.2e-19

# Masas de las particulas a utilizar
M_electron = 9.109e-31
M_positron = 9.109e-31
M_proton = 1.675e-27
M_neutron = 1.675e-27
M_particulaAlfa = 6.696e-27
M_nucleoDeDeuterio = 3.348e-27
M_muon = 1.880e-25
M_antimuon = 1.880e-25
M_positron = 0 #falta
M_positron = 0 #falta


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
Ingrese la opcion que desea usar:  \n''')
    if cat=='2':
        print("")
        print("Gracias por hacer uso del programa")
        break
    if cat=='1':
        #ingreso de los valores de la velociadad inicial
        print("Ingrese los siguientes valores \n\n")
        while True:
            try:
                VelDir = float(input("Ingrese la VELOCIDAD INICIAL DE LA PARTICULA: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        while True:
            try:
                VelMagnitud = float(input("Ingrese EL ANGULO DE DISPARO DE 0 A 90 GRADOS: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        
        #ingreso de los valores del campo electrico
        
       #print("Ingrese los valores del CAMPO ELECTRICO")
        #magnitud del campo
        while True:
            try:
                CampoMagnitud = float(input("Ingrese la MAGNITUD del CAMPO ELECTRICO: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        #sentido del campo
        while True:
            try:
                print("Ingrese una de las opciones (1 o 2) para el SENTIDO del CAMPO ELECTRICO: ")
                print("1. Eje y positivo")
                print("2. Eje y negativo")
                CampoSentido = int(input("Ingrese la opcion"))
                break
            except:
                print("Ingrese Un valor Valido\n")
#         #largo del campo, lo comente porque creo que no hace falta el largo
#         while True:
#             try:
#                 CampoLargo = float(input("Ingrese el LARGO del CAMPO ELECTRICO: "))
#                 break
#             except:
#                 print("Ingrese Un valor Valido")
        #ancho del campo
        while True:
            try:
                CampoAncho = float(input("Ingrese el ANCHO del CAMPO ELECTRICO:"))
                break
            except:
                print("Ingrese Un valor Valido\n")
        print("\n")
       #tipo de particula
        print("Escoga la particula a utilizar \n")
        print("1. Electron")
        print("2. Positron")
        print("3. Proton")
        print("4. Neutron ")
        print("5. Particula alfa ")
        print("6. Nucleo de Deuterio ")
        print("7. Muon ")
        print("8. Antimuon")
        print("9. ")
        print("10. ")
        
        while True:
            try:
                ParticulaTipo = int(input("Ingrese opcion"))
                break
            except:
                print("Ingrese Una opcion Valida\n")
        while True:
            try:
                ParticulaCantidad = int(input("Ingrese el NUMERO DE PARTIULAS que desea usar: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        
        #333333333333333
        print(M_electron)
    
