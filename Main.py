#JuanMarroquin 19845
#Carlos Raxtum 19721

import calculos as calcu
# Cargas a utilizar
C_neutra = 0 
C_positiva = 1.6e-19 #medida en C
C_negativa = -1.6e-19
C_alfa = 3.2e-19

dicc_particulas = {"Electron": 9.109e-31,#masas, medida en Kilogramo
                   "Positron" : 9.109e-31,
                   "Proton" : 1.675e-27,
                   "Neutron": 1.675e-27,
                   "ParticulaAlfa": 6.696e-27,
                   "NucleoDeDeuterio": 3.348e-27,
                   "Muon": 1.880e-25,
                   "Antimuon": 1.880e-25,
                   "sabes": 0, #falta
                   "saber": 0, #falta
                    }



print('''Bienvenido
Al programa grafica una particula en un campo electrico ''')


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
        #tipo de particula
        print("\n")
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
                ParticulaTipo = int(input("Ingrese opcion: "))
                if ParticulaTipo == 1:
                    #obtener el valor de carga
                    masa = dicc_particulas["Electron"]
                elif ParticulaTipo == 2:
                    #obtener el valor de carga
                    masa = dicc_particulas["Positron"]
                elif ParticulaTipo == 3:
                    #obtener el valor de carga
                    masa = dicc_particulas["Proton"]
                elif ParticulaTipo == 4:
                    #obtener el valor de carga
                    masa = dicc_particulas["Neutron"]
                elif ParticulaTipo == 5:
                    #obtener el valor de carga
                    masa = dicc_particulas["ParticulaAlfa"]
                elif ParticulaTipo == 6:
                    #obtener el valor de carga
                    masa = dicc_particulas["NucleoDeDeuterio"]
                elif ParticulaTipo == 7:
                    #obtener el valor de carga
                    masa = dicc_particulas["Muon"]
                elif ParticulaTipo == 8:
                    #obtener el valor de carga
                    masa = dicc_particulas["Antimuon"]
                elif ParticulaTipo == 9:
                    #obtener el valor de carga
                    masa = dicc_particulas["saber"]
                elif ParticulaTipo == 10:
                    #obtener el valor de carga
                    masa = dicc_particulas["saber"]
                    
                break
            except:
                print("Ingrese Una opcion Valida\n")
        print("La masa de la particula seleccionada es: ",masa)
        while True:
            try:
                ParticulaCantidad = int(input("Ingrese el NUMERO DE PARTIULAS que desea usar: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        #ingreso de los valores de la velociadad inicial
        while True:
            try:
                velocidad = float(input("Ingrese la VELOCIDAD INICIAL DE LA PARTICULA: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        while True:
            try:
                angulo = float(input("Ingrese EL ANGULO DE DISPARO DE 0 A 90 GRADOS: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        
        #ingreso de los valores del campo electrico
        
       #print("Ingrese los valores del CAMPO ELECTRICO")
        #magnitud del campo
        while True:
            try:
                CMagnitud = float(input("Ingrese la MAGNITUD del CAMPO ELECTRICO: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        #sentido del campo
        while True:
            try:
                print("Ingrese una de las opciones (1 o 2) para el SENTIDO del CAMPO ELECTRICO: ")
                print("1. Eje y positivo")
                print("2. Eje y negativo")
                CSentido = int(input("Ingrese la opcion: "))
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
                CampoLargo = float(input("Ingrese el Largo del CAMPO ELECTRICO: "))
                break
            except:
                print("Ingrese Un valor Valido\n")
        #333333333333333
        
        calcu.prueba(1)
