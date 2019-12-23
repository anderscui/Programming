package andersc.tour.values

fun main() {
    // #1: safe call
    var beverage = readLine()?.capitalize()
    println(beverage)

    // let
    beverage = readLine()?.let {
        if (it.isNotBlank()) {
            it.capitalize()
        } else {
            "Buttered Ale"
        }
    }
    println(beverage)

    // #2:
    beverage = readLine()!!.capitalize()
    println(beverage)

    // #3: if-else

    // null coalescing
    val beverageServed = beverage ?: "Buttered Ale"
}
