package andersc.tour.values

import andersc.tour.values.extensions.random

class Dice() {
    val rolledValue
        get() = (1..6).random()
}
