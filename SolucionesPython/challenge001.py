"""""
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""

def checkAnagrams(word1,word2):
    word1_or = sorted(word1.lower())
    word2_or = sorted(word2.lower())

    if (word1_or == word2_or):
        return True
    else:
        return False


def run():
    word1 = input("Ingresa la primer palabra: ")
    word2 = input("Ingresa la segunda palabra: ")
    print("-------------------------------------")
    print("Iniciando comprobacion si las dos palabras son anagramas")
    if (word1 == word2):
        print("NO se aceptan dos palabras iguales")
    elif (checkAnagrams(word1,word2)):
        print("Las palabras SI son un anagrama")
    else:
        print("Las palabras NO son un anagrama")


if __name__ == '__main__':
    run()
    