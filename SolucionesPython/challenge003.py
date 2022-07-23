"""
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""

def printPrimeNumbers(n):
    if (n==2 or n ==3 or n == 5 or n == 7):
        return True
    elif (n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n == 1):
        return False
    else:
        return True
    

def run():
    for i in range(1,100):
        if (printPrimeNumbers(i)):
            print(i)
        else:
            continue


if __name__ == '__main__':
    run()

