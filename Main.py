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
                   "NeutrinoMuonico": 3.38e-31,
                   "Muon": 1.880e-25,
                   "Antimuon": 1.880e-25,
                   "Tauón": 3.167e-27, 
                   "Antitauón": 3.167e-27, 
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
        print("6. Neutrino Muonico ")
        print("7. Muon ")
        print("8. Antimuon")
        print("9. Tauón")
        print("10. AntiTauón")
        
        while True:
            try:
                ParticulaTipo = int(input("Ingrese opcion"))
                if ParticulaTipo == 1:
                    #obtener el valor de carga
                    masa = dicc_particulas["Electron"]
                    carga = -1.6e-19
                elif ParticulaTipo == 2:
                    #obtener el valor de carga
                    masa = dicc_particulas["Positron"]
                    carga = 1.6e-19
                elif ParticulaTipo == 3:
                    #obtener el valor de carga
                    masa = dicc_particulas["Proton"]
                    carga = 1.6e-19
                elif ParticulaTipo == 4:
                    #obtener el valor de carga
                    masa = dicc_particulas["Neutron"]
                    carga = 0
                elif ParticulaTipo == 5:
                    #obtener el valor de carga
                    masa = dicc_particulas["ParticulaAlfa"]
                    carga = 3.2e-19
                elif ParticulaTipo == 6:
                    #obtener el valor de carga
                    masa = dicc_particulas["NeutrinoMuonico"]
                    carga = -1.6e-19
                elif ParticulaTipo == 7:
                    #obtener el valor de carga
                    masa = dicc_particulas["Muon"]
                    carga = -1
                elif ParticulaTipo == 8:
                    #obtener el valor de carga
                    masa = dicc_particulas["Antimuon"]
                    carga = +1
                elif ParticulaTipo == 9:
                    #obtener el valor de carga
                    masa = dicc_particulas["Tauón"]
                    carga = -1
                elif ParticulaTipo == 10:
                    #obtener el valor de carga
                    masa = dicc_particulas["Antitauón"]
                    carga = +1
                    
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
                CampoSentido = int(input("Ingrese la opcion: "))
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
        #Variables y llamado de funciones que ayudan a encontrar la grafica
        
        #calculo masa total
        MasaTotal = masa*ParticulaCantidad
        #calculo carga total
        CargaTotal = ParticulaCantidad*carga
        #calculo campo electrico
        CampoElectrico = calcu.CampoElec(CMagnitud,CampoSentido)
        #calculo aceleracion
        Aceleracion = calcu.Aceleracion(CargaTotal,CampoElectrico,MasaTotal)
        #graficar
        calcu.Graficar(Aceleracion,angulo,velocidad,CampoLargo)