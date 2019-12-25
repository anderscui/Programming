@file:JvmName("Hero")
package andersc.tour.values.interops

import andersc.tour.values.show

fun main() {
    val adversary = Jhava()
    adversary.greeting = "Hello, hero."
    adversary.utterGreeting().show()

    val level = adversary.determineLevel()
    (level?.toLowerCase() ?: "Unknown value").show()

    val points = adversary.hitPoints
    points.dec().show()
    points.javaClass.show()
}

fun makeProclamation() = "Greetings, beast."

@JvmOverloads
fun handOverFood(leftHand: String = "berries", rightHand: String = "beef") {
    println("Mmmm... you hand over some delicious $leftHand and $rightHand")
}
