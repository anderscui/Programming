package andersc.tour.pro

class Companions {
    fun run() {
        println("Hello world")
    }

    companion object {
        @JvmStatic fun main(array: Array<String>) {
            Companions().run()
        }
    }
}