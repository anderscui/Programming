package andersc.tour.pro

fun plus2(x: Int) = x + 2

// shorthand fun
fun alwaysFunny() = "fun"

// inline fun
inline fun sayMyName(name: String) = "Your name is $name"

// higher order
fun twice(x: () -> Any?) {
    x(); x();
}

fun main() {
    // fun ref
    println(listOf(1, 2, 3, 4, 5).map(::plus2))

    println(alwaysFunny())

    val strs = listOf("a", "bc", "def")
    // if the only arg is a lambda fun，笑容逐渐凝固
    println(strs.map({ item: String -> item.length }))
    println(strs.map({ item -> item.length }))
    println(strs.map({ it.length }))
    println(strs.map{ it.length })
    println(strs.filter { it.length >= 2 })

    // taking other funs
    twice { println("foo") }
}

