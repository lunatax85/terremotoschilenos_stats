import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

x = datos_sismos['Long']  # Longitud
y = datos_sismos['Lat']   # Latitud
z = datos_sismos['Magnitud']  # Magnitud

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(x, y, z, c=z, cmap='viridis', label='Sismos')

ax.set_title('Visualización 3D de Sismos')

ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
ax.set_zlabel('Magnitud')

def on_click(event):
    if event.inaxes != ax:
        return

    x2, y2, _ = event.xdata, event.ydata, event.zdata
    

    x2, y2, z2 = ax.transData.transform((x2, y2, 0))
    

    distances = (x - x2)**2 + (y - y2)**2 + (z - z2)**2
    min_dist_index = distances.argmin()
    closest_point = datos_sismos.iloc[min_dist_index]

    ax.annotate(f'Magnitud: {closest_point["Magnitud"]}\nFecha: {closest_point["Fecha"]}', 
                xy=(closest_point["Long"], closest_point["Lat"]), 
                xytext=(3, 3),
                textcoords='offset points',
                arrowprops=dict(facecolor='black', shrink=0.05))

    plt.draw()

fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()
