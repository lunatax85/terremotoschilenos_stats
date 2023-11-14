def leer_datos_sismos(nombre_archivo):
    archivo = open(nombre_archivo)
    datos = []
    for linea in archivo:
        linea = linea.rstrip('\n')
        lista = linea.split(',')
        datos.append(lista)
    archivo.close()
    return datos

def encontrar_mayor_sismo(datos):
    mayor_magnitud = 0
    fecha_hora_mayor = ""

    for dato in datos:
        magnitud_str = dato[4]
        if magnitud_str != '-':
            magnitud = float(magnitud_str)
            fecha = dato[0]
            hora = dato[1]

            if magnitud > mayor_magnitud:
                mayor_magnitud = magnitud
                fecha_hora_mayor = f"Fecha: {fecha} y hora: {hora}"

    return fecha_hora_mayor

def contar_sismos_magnitud(datos, magnitud_min, magnitud_max=None):
    contador_sismos = 0

    for dato in datos:
        magnitud_str = dato[4]
        if magnitud_str != '-':
            magnitud = float(magnitud_str)

            if magnitud_max is None:
                if magnitud >= magnitud_min:
                    contador_sismos += 1
            else:
                if magnitud >= magnitud_min and magnitud < magnitud_max:
                    contador_sismos += 1

    return contador_sismos

def contar_sismos_por_siglo(datos):
    contador_sismos_siglo = {16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0}

    for dato in datos:
        anio = int(dato[0].split('-')[2])
        siglo = (anio // 100) + 1

        if siglo in contador_sismos_siglo:
            contador_sismos_siglo[siglo] += 1

    return contador_sismos_siglo

archivo_sismos = 'sismos.txt'

datos_sismos = leer_datos_sismos(archivo_sismos)

magnitud_min_1 = 7.0
magnitud_max_1 = 8.0
cantidad_sismos_1 = contar_sismos_magnitud(datos_sismos, magnitud_min_1, magnitud_max_1)

magnitud_min_2 = 8.0
magnitud_max_2 = 9.0
cantidad_sismos_2 = contar_sismos_magnitud(datos_sismos, magnitud_min_2, magnitud_max_2)

magnitud_min_3 = 9.0
cantidad_sismos_3 = contar_sismos_magnitud(datos_sismos, magnitud_min_3)

contador_sismos_siglo = contar_sismos_por_siglo(datos_sismos)

fecha_hora_mayor_sismo = encontrar_mayor_sismo(datos_sismos)
print("La", fecha_hora_mayor_sismo, "del mayor sismo registrado.")
print(f"Cantidad de sismos >= {magnitud_min_1} y < {magnitud_max_1}: {cantidad_sismos_1}")
print(f"Cantidad de sismos >= {magnitud_min_2} y < {magnitud_max_2}: {cantidad_sismos_2}")
print(f"Cantidad de sismos >= {magnitud_min_3}: {cantidad_sismos_3}")
for siglo, cantidad in contador_sismos_siglo.items():
    print(f"Cantidad de sismos siglo {siglo}: {cantidad}")