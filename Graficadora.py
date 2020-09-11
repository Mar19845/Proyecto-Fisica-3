# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# from matplotlib import style
from numpy import linspace, sin, cos
from pylab import figure, show
from mpl_toolkits.mplot3d import Axes3D

# # generando algunos datos
x = linspace(-10,10,100);
y = sin(x);
z = cos(x);

# # Se crea la instancia de la figura y se asocia a la figura 3D

fig = figure()
ax = Axes3D(fig)


# # graficando los datos
for i in range(len(x)):
  ax.plot([x[i], x[i]], [y[i], y[i]], [0, z[i]], 
          '--', linewidth=2, color='b', alpha=.5)

# # graficando un circulo en el tope de cada curva
# plotting a circle on the top of each stem
ax.plot(x, y, z, 'o', markersize=8, 
        markerfacecolor='none', color='b',label='ib')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

show()

# 
# # Creamos la figura
# fig = plt.figure()
# 
# # Agrrgamos un plano 3D
# ax1 = fig.add_subplot(111,projection='3d')
# 
# # Mostramos el gráfico
# plt.show()

#!/usr/bin/env python3

# # Se importan las librerías necesarias
