from msilib.schema import Condition
import string

from direccion import direccion


print("Hola usuario, a continuacion le mostrare varias opciones las cuales podra hacer en la aplicacion")
print("pulse 1: para mostrar la lista de direcciones guardadas")
print("pulse 2: para guardar una direccion especifica")
print("pulse 3: para ingresar la direccion en la que esta y a la cual se dirige")
print("pulse 4: para salir")

condicion = int(input())
if condicion  == 1:
    
 def abrir(ruta):
    archivo = open(ruta)
    texto = archivo.read()
    archivo.close()
    return texto


def obtener_direciones(archivo):
    lista_direcciones = []
    lineas = archivo.splitlines()
    
    for linea in lineas:
       
        nombre, origen, destino, tamano, sentido, riesgoacoso, geometria = linea.split(";")
        
        direccionMapa = direccion()
        direccionMapa.nombre(nombre)
        direccionMapa.origen(origen)
        direccionMapa.destino(destino)
        direccionMapa.tamano(tamano)
        direccionMapa.sentido(sentido)
        direccionMapa.riesgoacoso(riesgoacoso)
        direccionMapa.geometria(geometria)
        lista_direcciones.append(direccionMapa)
        print (linea)
    return lista_direcciones

def main():
 ruta = ("C:\mapaestructura\mapa.csv")
 archivo = abrir(ruta)
 lista_direciones = obtener_direciones(archivo)
 print (lista_direciones)
 
if condicion == 4:
    quit()
 
main()