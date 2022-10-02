import string

from direccion import direccion


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
 
main()