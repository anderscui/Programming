package andersc.tour.pro

fun main() {
    // empty array
    val empty = emptyArray<String>()
    println(empty)

    val strs = Array(size = 5, init = { index -> "Item #$index"})
    println(strs.toString())
    println(strs[0])

    val ints = intArrayOf(1, 2, 3)
    println(ints)

    // create using closure
    val a = Array(3) { i -> i * 2}

    // extensions
    println("average: ${a.average()}, first: ${a.firstOrNull()}")

    // iterate
    for (i in a) {
        print(i)
        print(' ')
    }
}