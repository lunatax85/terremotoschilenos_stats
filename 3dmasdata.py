import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def leer_datos_sismos(nombre_archivo):
    try:
        datos_sismos = pd.read_csv(
            nombre_archivo, 
            delimiter=',', 
            header=None, 
            names=['Fecha', 'Hora', 'Lat', 'Long', 'Magnitud'],
            on_bad_lines='skip' 
        )
      
        datos_sismos['Magnitud'] = pd.to_numeric(datos_sismos['Magnitud'], errors='coerce')
        return datos_sismos
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")
        return None


nombre_archivo = 'C:/DESARROLLO/terremotoschilenos_stats/sismos.txt'


datos_sismos = leer_datos_sismos(nombre_archivo)


if datos_sismos is not None:
    print("Datos leídos correctamente:")
    print(datos_sismos.head())  
else:
    print("No se pudieron leer los datos.")


def sismo_mayor_magnitud(datos_sismos):
    return datos_sismos.loc[datos_sismos['Magnitud'].idxmax()]

def contar_sismos_rango_magnitud(datos_sismos, min_magnitud, max_magnitud):
    return datos_sismos[(datos_sismos['Magnitud'] >= min_magnitud) & (datos_sismos['Magnitud'] < max_magnitud)].shape[0]

def sismos_por_siglo(datos_sismos):
   
    try:
        siglos = datos_sismos['Fecha'].str.extract(r'(\d{4})')[0]
        siglos = pd.to_numeric(siglos, errors='coerce')
        siglos = (siglos - 1) // 100 + 1
        return siglos.value_counts().sort_index()
    except Exception as e:
        print(f"Error al procesar los siglos: {e}")
        return None



mayor_sismo = sismo_mayor_magnitud(datos_sismos)
print(f"Fecha: {mayor_sismo['Fecha']} y hora: {mayor_sismo['Hora']} del mayor sismo registrado.")

for rango in [(7.0, 8.0), (8.0, 9.0), (9.0, float('inf'))]:
    count = contar_sismos_rango_magnitud(datos_sismos, *rango)
    print(f"Cantidad de sismos >= {rango[0]} y < {rango[1] if rango[1] != float('inf') else 'infinito'}: {count}")

siglos_sismos = sismos_por_siglo(datos_sismos)
for siglo, count in siglos_sismos.items():
    print(f"Cantidad de sismos siglo {siglo}: {count}")


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')


datos_sismos = datos_sismos.dropna(subset=['Magnitud']) 
x = datos_sismos['Long']
y = datos_sismos['Lat']
z = datos_sismos['Magnitud']


scatter = ax.scatter(x, y, z, c=z, cmap='viridis', label='Sismos')


ax.set_title('Visualización 3D de Sismos')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
ax.set_zlabel('Magnitud')


plt.show()
