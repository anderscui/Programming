package andersc.tour.pro

fun compareStrs(s1: String, s2: String): Boolean {
    return s1 == s2
}

fun compareRefs(s1: String, s2: String): Boolean {
    return s1 === s2
}

fun main() {
    println(compareStrs("Hello world", "Hello " + "world"))

    val lines = """
        for i in range(10):
            print(i)
    """.trim()
    println(lines)
}