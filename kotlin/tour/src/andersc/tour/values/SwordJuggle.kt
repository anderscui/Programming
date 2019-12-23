package andersc.tour.values

import java.lang.Exception
import java.lang.IllegalStateException

fun main() {
    var swordsJuggling: Int? = null
    val isJuggleProficient = (1..3).shuffled().last() == 3
    if (isJuggleProficient) {
        swordsJuggling = 2
    }
    try {
        proficiencyCheck(swordsJuggling)
        swordsJuggling = swordsJuggling!!.plus(1)
    } catch (e: Exception) {
        println(e)
    }

    println("You juggle $swordsJuggling swords.")
}

fun proficiencyCheck(swordsJuggling: Int?) {
    // swordsJuggling ?: throw UnskilledSwordJugglerException()
    checkNotNull(swordsJuggling, { "Player cannot juggle swords." })
}

class UnskilledSwordJugglerException(): IllegalStateException("Player cannot juggle swords.")
