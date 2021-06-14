package andersc.tour.pro

fun main(args: Array<String>) {
    println("Enter two numbers")
    val (a, b) = readLine()!!.split(' ')
    println("Max number is: ${maxNum(a.toInt(), b.toInt())}")
}

fun maxNum(a: Int, b: Int): Int {
    return if (a > b) {
        a
    } else {
        b
    }
}