#Datos que sabemos
#velocidad inicial de la particula
#Masa de la particula, carga de particula
#Angulo de disparo
#Magnitud del campo electrico
#Sentido del campo electrico
#Ancho del campo elecrico

def CampoElec (CMagnitud, CSentido, carga): # calculo del campo electrico f = qE; E = f/q, donde F = magnitud, q = carga paticula y E campo electrico
    campo_electrico = CMagnitud/carga
    if CampoSentido == 0:
        #campo electrico positivo en y
    else
        #campo electrico negativo en y
    return campo_electrico

def Aceleracion (carga, campo_electrico, masa): #calculo de la aceleracion
    ace = (carga*campo_electrico/masa)
    return ace



def Tiempo (): # calculo del tiempo
    




def Posicion_x (velocidad, angulo, tiempo): #calculo de la posicion en y
    y = velocidad * np.sin(angulo) * tiempo(desplazamiento_x, velocidad, )



def Posicion_y (desplazamiento_x, velocidad, angulo, campo_electrico): #calculo de la posicion en y  
    y = velocidad * np.sin(angulo) * tiempo(desplazamiento_x, velocidad, )
    