"""
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""

def polygonArea(polygon,a,b):
    """
    Description: Function in charge of calculating the area of three polygons (Triangle, Rectangle and Square)
    Inputs: 
        polygon: 
    """
    pol_area = {
        "Triangle" : a*b/2,
        "Rectangle" : a*b,
        "Square" : a*a
    }
     
    area = pol_area.get(polygon)
    message = "The {0} area is {1}".format(polygon,str(area))
    return area, message


def run():
    print(polygonArea("Triangle",2.5,5)[1])
    print(polygonArea("Rectangle",2.0,5)[1])
    print(polygonArea("Square",2.5,0)[1])


if __name__ == '__main__':
    run()
