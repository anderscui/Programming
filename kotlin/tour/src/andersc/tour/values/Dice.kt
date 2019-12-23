package andersc.tour.values

class Dice() {
    val rolledValue
        get() = (1..6).shuffled().first()
}
