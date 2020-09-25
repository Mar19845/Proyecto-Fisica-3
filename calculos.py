#Datos que sabemos
#velocidad inicial de la particula
#Masa de la particula, carga de particula
#Angulo de disparo
#Magnitud del campo electrico
#Sentido del campo electrico
#Ancho del campo elecrico
import math
def prueba(hola):
    print("esto funciona")
    
#funcion que calcula la tangente del angulo
def tan(grados):
     return math.tan(math.radians(grados))
    
#funcion que calcula 3l coseno del angulo
def cos(grados):
     return math.cos(math.radians(grados))

def CampoElec (CMagnitud, CSentido, carga): # calculo del campo electrico f = qE; E = f/q, donde F = magnitud, q = carga paticula y E campo electrico
    campo_electrico = CMagnitud/carga
    if CampoSentido == 0:
        campo_electrico=1
        #campo electrico positivo en y
    else:
        campo_electrico=2
        #campo electrico negativo en y
    return campo_electrico

def Aceleracion (carga, campo_electrico, masa): #calculo de la aceleracion
    ace = (carga*campo_electrico/masa)
    return ace

#funcion que se encarga de graficar la solucion
def Graficar(aceleracion,angulo,vel,distancia):
    tangente = tan(angulo)
    coseno = cos(angulo)
    y= tangente*x + (aceleracion/(2*(velocidad**2)*(coseno**2)))*(x**2)

#def Posicion_x (velocidad, angulo, tiempo): #calculo de la posicion en y
#    y = velocidad * np.sin(angulo) * tiempo(desplazamiento_x, velocidad, )



#def Posicion_y (desplazamiento_x, velocidad, angulo, campo_electrico): #calculo de la posicion en y  
#    y = velocidad * np.sin(angulo) * tiempo(desplazamiento_x, velocidad, )
    
