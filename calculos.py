#Datos que sabemos
#velocidad inicial de la particula
#Masa de la particula, carga de particula
#Angulo de disparo
#Magnitud del campo electrico
#Sentido del campo electrico
#Ancho del campo elecrico

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca()

    
#funcion que calcula la tangente del angulo
def tan(grados):
     return math.tan(math.radians(grados))
    
#funcion que calcula 3l coseno del angulo
def cos(grados):
     return math.cos(math.radians(grados))

def CampoElec (CMagnitud, CampoSentido, ):
    
    
    if CampoSentido == 1:
        campo_electrico=1*CMagnitud
        #campo electrico positivo en y
    if CampoSentido == 2:
        campo_electrico=-1*CMagnitud
        #campo electrico negativo en y
        
    return campo_electrico

def Aceleracion (carga, campo_electrico, masa): #calculo de la aceleracion
    ace = (carga*campo_electrico/masa)
    return ace

#funcion que se encarga de graficar la solucion
def Graficar(aceleracion,angulo,velocidad,distancia):
    
    tangente = tan(angulo)
    coseno = cos(angulo)
    
    x = np.linspace(0,distancia,200)
    y= tangente*x + (aceleracion/(2*(velocidad**2)*(coseno**2)))*(x**2)
    
    def actualizar(i):
        ax.clear()
        ax.plot(x[:i],y[:i])
        plt.title("Posicion de X contra Y")
        plt.xlabel("Posicion en X (m)")
        plt.ylabel("Posicion en Y (m)")
        plt.xlim(min(x),2*max(x))
        plt.ylim(min(y),max(y))
        
    
    ani = animation.FuncAnimation(fig,actualizar,range(len(x)),interval = 20,repeat = False)
    plt.show()
    
#def Posicion_x (velocidad, angulo, tiempo): #calculo de la posicion en y
#    y = velocidad * np.sin(angulo) * tiempo(desplazamiento_x, velocidad, )



#def Posicion_y (desplazamiento_x, velocidad, angulo, campo_electrico): #calculo de la posicion en y  
#    y = velocidad * np.sin(angulo) * tiempo(desplazamiento_x, velocidad, )
    
