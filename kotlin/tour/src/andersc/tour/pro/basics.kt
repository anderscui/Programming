package andersc.tour.pro

fun printHello(name: String?): Unit {
    if (name != null) {
        println("Hello $name")
    }
}

// single exp fun
fun double(x: Int): Int = x * 2

