import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from collections import Counter

# Funciones leer_datos_sismos, obtener_magnitud, sismo_mayor_magnitud, contar_sismos_rango_magnitud y sismos_por_siglo permanecen sin cambios.

# Función para graficar los sismos en 3D
def graficar_sismos_3d(datos_sismos):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Preparar los datos de sismos para la visualización
    siglos_sismos = sismos_por_siglo(datos_sismos)
    siglos_ordenados = sorted(siglos_sismos.items())
    siglos = [siglo for siglo, _ in siglos_ordenados]
    conteos = [conteo for _, conteo in siglos_ordenados]
    
    # Configurar los colores según la magnitud del sismo
    colores = plt.cm.viridis(np.linspace(0, 1, len(conteos)))
    
    # Graficar los datos en 3D
    xs = np.arange(len(siglos))
    ys = [5] * len(siglos)  # Un valor arbitrario para Y, ya que solo estamos interesados en X y Z
    zs = conteos
    
    for x, y, z, color in zip(xs, ys, zs, colores):
        ax.bar3d(x, y, 0, 1, 1, z, color=color)

    # Establecer etiquetas para los ejes
    ax.set_xticks(xs + 0.5)
    ax.set_xticklabels([f'Siglo {siglo}' for siglo in siglos])
    ax.set_xlabel('Siglo')
    ax.set_ylabel('Escala Arbitraria')
    ax.set_zlabel('Cantidad de Sismos')

    # Establecer el título del gráfico
    ax.set_title('Cantidad de Sismos por Siglo')

    # Mostrar el gráfico
    plt.show()

# Funciones calcular_estadisticas y mostrar_resultados permanecen sin cambios.

# Principal ejecución del código
if __name__ == '__main__':
    datos_sismos = leer_datos_sismos('C:/DESARROLLO/terremotoschilenos_stats/sismos.txt')
    resultados = calcular_estadisticas(datos_sismos)
    mostrar_resultados(resultados)
    graficar_sismos_3d(datos_sismos)  # Llamada a la función de visualización 3D
