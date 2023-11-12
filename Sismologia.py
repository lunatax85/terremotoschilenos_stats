import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from collections import Counter


def leer_datos_sismos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = archivo.readlines()
    return [linea.strip().split(',') for linea in datos]

def sismo_mayor_magnitud(datos_sismos):
    mayor_magnitud = max(datos_sismos, key=lambda x: float(x[4]))
    return mayor_magnitud[0], mayor_magnitud[1]

def contar_sismos_rango_magnitud(datos_sismos, min_magnitud, max_magnitud):
    return sum(min_magnitud <= float(sismo[4]) < max_magnitud for sismo in datos_sismos if sismo[4] not in ['-', ''])

def sismos_por_siglo(datos_sismos):
    siglos = Counter()
    for sismo in datos_sismos:
        if sismo[0] not in ['-', '']:
            siglo = (int(sismo[0].split('-')[2]) - 1) // 100 + 1
            siglos[siglo] += 1
    return siglos

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

def graficar_sismos_3d(siglos):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    siglos_ordenados = sorted(siglos.items())
    siglos = [siglo for siglo, _ in siglos_ordenados]
    magnitudes = [float(magnitud) for _, magnitud in siglos_ordenados]
    conteos = [conteo for _, conteo in siglos_ordenados]

    # Coordenadas x, y, y z de las barras
    x = [i for i in range(len(siglos))]
    y = magnitudes
    z = np.zeros_like(x)  # Posición en el eje z (todos en el mismo plano)

    # Dimensiones de las barras
    dx = dy = 0.8
    dz = conteos

    ax.bar3d(x, y, z, dx, dy, dz, shade=True)

    # Ajustar etiquetas del eje x para reflejar los siglos
    ax.set_xticks(x)
    ax.set_xticklabels(siglos)

    ax.set_xlabel('Siglo')
    ax.set_ylabel('Magnitud del Sismo')
    ax.set_zlabel('Cantidad de Sismos')
    ax.set_title('Cantidad de Sismos por Siglo y Magnitud')

    plt.show()

def calcular_estadisticas(datos_sismos):
    fecha_hora_mayor_sismo = sismo_mayor_magnitud(datos_sismos)
    sismos_7_8 = contar_sismos_rango_magnitud(datos_sismos, 7.0, 8.0)
    sismos_8_9 = contar_sismos_rango_magnitud(datos_sismos, 8.0, 9.0)
    sismos_mayor_9 = contar_sismos_rango_magnitud(datos_sismos, 9.0, float('inf'))
    
    siglos_sismos = sismos_por_siglo(datos_sismos)
    
    return fecha_hora_mayor_sismo, sismos_7_8, sismos_8_9, sismos_mayor_9, siglos_sismos

def mostrar_resultados(resultados):
    fecha_hora_mayor_sismo, sismos_7_8, sismos_8_9, sismos_mayor_9, siglos_sismos = resultados

    print(f"Fecha: {fecha_hora_mayor_sismo[0]} y hora: {fecha_hora_mayor_sismo[1]} del mayor sismo registrado.")
    print(f"Cantidad de sismos >= 7.0 y < 8.0: {sismos_7_8}")
    print(f"Cantidad de sismos >= 8.0 y < 9.0: {sismos_8_9}")
    print(f"Cantidad de sismos >= 9.0: {sismos_mayor_9}")

    # Imprimir la cantidad de sismos por siglo
    for siglo in range(16, 22):
        print(f"Cantidad de sismos siglo {siglo}: {siglos_sismos.get(siglo, 0)}")

    # Graficar los sismos por siglo en 3D
    graficar_sismos_3d(siglos_sismos)

if __name__ == '__main__':
    datos_sismos = leer_datos_sismos('C:/DESARROLLO/terremotoschilenos_stats/sismos.txt')
    resultados = calcular_estadisticas(datos_sismos)
    mostrar_resultados(resultados)