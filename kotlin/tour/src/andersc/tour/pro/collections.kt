package andersc.tour.pro

fun main() {
    // kt distinguishes mutable and immutable collections
    // a readonly list
    val list = listOf("a", "b")
    println(list)

    val map = mapOf(Pair("a", 1), Pair("b", 2))
    println(map)

    val set = setOf(1, 3, 5)
    println(set)
}