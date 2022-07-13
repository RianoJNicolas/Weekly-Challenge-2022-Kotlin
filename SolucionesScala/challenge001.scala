/*
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
*/
import java.util.Arrays

def checkAnagrams(word1: String, word2: String) = {
    val word1_or = word1.toLowerCase.toCharArray().sorted
    val word2_or = word2.toLowerCase.toCharArray().sorted

    if (word1.toLowerCase == word2.toLowerCase) {
        println("No se aceptan dos palabras iguales")
    }
    else if (Arrays.equals(word1_or,word2_or)) {
        println("Las palabras SI son anagramas")
    }
    else {
        println("Las palabras NO son anagramas")
    }
}

val word1 = "AMOR"
val word2 = "RomA"

checkAnagrams(word1,word2)