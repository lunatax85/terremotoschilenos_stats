import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from collections import Counter

# Función para leer los datos del archivo de sismos
def leer_datos_sismos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = archivo.readlines()
    return [linea.strip().split(',') for linea in datos]

# Función para encontrar el sismo de mayor magnitud
def sismo_mayor_magnitud(datos_sismos):
    mayor_magnitud = max(datos_sismos, key=lambda x: float(x[4]))
    return mayor_magnitud[0], mayor_magnitud[1]

# Función para contar sismos en un rango de magnitud
def contar_sismos_rango_magnitud(datos_sismos, min_magnitud, max_magnitud):
    return sum(min_magnitud <= float(sismo[4]) < max_magnitud for sismo in datos_sismos if sismo[4] not in ['-', ''])

# Función para contar sismos por siglo
def sismos_por_siglo(datos_sismos):
    siglos = Counter()
    for sismo in datos_sismos:
        if sismo[0] not in ['-', '']:
            siglo = (int(sismo[0].split('-')[2]) - 1) // 100 + 1
            siglos[siglo] += 1
    return siglos

# Función para graficar sismos por siglo en 2D
def graficar_sismos_por_siglo(siglos):
    siglos_ordenados = sorted(siglos.items())
    siglos = [f'Siglo {siglo}' for siglo, _ in siglos_ordenados]
    conteos = [conteo for _, conteo in siglos_ordenados]
    
    plt.figure(figsize=(10, 6))
    plt.bar(siglos, conteos, color='skyblue')
    plt.title('Cantidad de Sismos por Siglo')
    plt.xlabel('Siglo')
    plt.ylabel('Cantidad de Sismos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Función para graficar sismos en 3D con fondo de imagen
def graficar_sismos_3d(siglos):
    fig = plt.figure(figsize=(12, 8))
    
    # Cargar y establecer la imagen de fondo
    img = plt.imread('C:/desarrollo/terremotoschilenos_stats/fondo.png')
    fig.figimage(img, resize=True, alpha=0.5, zorder=1)

    # Crear los ejes 3D sobre la imagen
    ax = fig.add_subplot(111, projection='3d', zorder=2)

    siglos_ordenados = sorted(siglos.items())
    x = np.arange(len(siglos_ordenados))
    y = np.zeros(len(siglos_ordenados))
    z = np.zeros(len(siglos_ordenados))
    dx = np.ones(len(siglos_ordenados)) * 0.5
    dy = [float(magnitud) for _, magnitud in siglos_ordenados]
    dz = [conteo for _, conteo in siglos_ordenados]

    ax.bar3d(x, y, z, dx, dy, dz, alpha=0.6)

    ax.set_xticks(x)
    ax.set_xticklabels([f'Siglo {siglo}' for siglo, _ in siglos_ordenados])

    ax.set_xlabel('Siglo')
    ax.set_ylabel('Magnitud del Sismo')
    ax.set_zlabel('Cantidad de Sismos')
    ax.set_title('Cantidad de Sismos por Siglo y Magnitud')

    plt.show()

# Función para calcular estadísticas de los datos de sismos
def calcular_estadisticas(datos_sismos):
    fecha_hora_mayor_sismo = sismo_mayor_magnitud(datos_sismos)
    sismos_7_8 = contar_sismos_rango_magnitud(datos_sismos, 7.0, 8.0)
    sismos_8_9 = contar_sismos_rango_magnitud(datos_sismos, 8.0, 9.0)
    sismos_mayor_9 = contar_sismos_rango
