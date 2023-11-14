import matplotlib.pyplot as plt
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

if __name__ == '__main__':
    datos_sismos = leer_datos_sismos('C:/DESARROLLO/terremotoschilenos_stats/sismos.txt')



    fecha_hora_mayor_sismo = sismo_mayor_magnitud(datos_sismos)


    sismos_7_8 = contar_sismos_rango_magnitud(datos_sismos, 7.0, 8.0)
    sismos_8_9 = contar_sismos_rango_magnitud(datos_sismos, 8.0, 9.0)
    sismos_mayor_9 = contar_sismos_rango_magnitud(datos_sismos, 9.0, float('inf'))


    siglos_sismos = sismos_por_siglo(datos_sismos)

    print(f"Fecha: {fecha_hora_mayor_sismo[0]} y hora: {fecha_hora_mayor_sismo[1]} del mayor sismo registrado.")
    print(f"Cantidad de sismos >= 7.0 y < 8.0: {sismos_7_8}")
    print(f"Cantidad de sismos >= 8.0 y < 9.0: {sismos_8_9}")
    print(f"Cantidad de sismos >= 9.0: {sismos_mayor_9}")

    # Imprimir la cantidad de sismos por siglo
    for siglo in range(16, 22):
        print(f"Cantidad de sismos siglo {siglo}: {siglos_sismos.get(siglo, 0)}")

    # Graficar los sismos por siglo
    graficar_sismos_por_siglo(siglos_sismos)
