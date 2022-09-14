"""
 * Reto #5
 * ASPECT RATIO DE UNA IMAGEN
 * Fecha publicación enunciado: 01/02/22
 * Fecha publicación resolución: 07/02/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""

from PIL import Image
import urllib.request

# 1. Definicion de funciones
def getFileImage(url):
    fileImage = "image.png"
    urllib.request.urlretrieve(url,fileImage) 
    return fileImage


def getFeaturesImage(url):
    img = Image.open(getFileImage(url))
    w,h = img.size
    #print("el ancho de la imagen es: " + str(w))
    #print("el alto de la imagen es: " + str(h))
    return w,h


def calculateAR(width,hight):
    c_w = [i for i in range(1,width+1) if width%i == 0]
    c_h = [i for i in range(1,hight+1) if hight%i == 0]
    factorW = set(c_w)
    factorH = set(c_h)
    interSet = list(factorW & factorH) # Convierto en lista el resultado de la intersección de los dos conjuntos 
    factMax = max(interSet)
    arWidth = width/factMax
    arHight = hight/factMax
    message = "El aspect ratio de la imagen es: " + str(int(arWidth)) + ":" + str(int(arHight))
    return message, arWidth, arHight


# Funcion con el proceso importante
def run():
    width,hight = getFeaturesImage('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')
    print(calculateAR(width,hight)[0])


# Ejecucion
if __name__ == '__main__':
    run()
    

