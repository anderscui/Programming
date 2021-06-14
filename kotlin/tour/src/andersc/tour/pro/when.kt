package andersc.tour.pro

fun main() {
    // when matching
    val lan = "French"
    when (lan) {
        "English" -> println("How are you?")
        "French" -> println("Ca va bien?")
        else -> println("Je ne comprende pas.")
    }

    val names = listOf<String>("John", "Sarah", "Maggie")
    val item: Any = "item"
    when (item) {
        in names -> println("I know you")
        !in 1..10 -> println("Arg is not in the range")
        is String -> print(item.length) // smart casting
    }

    // `when` can be used as an expr.

    // `if` as an expr.
    val s = if (true) "true" else "false"

    // when branches
    when {
        s.length == 0 -> println("zero")
        s.length > 5 -> println("many")
        else         -> println("not bad")
    }
}