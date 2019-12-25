package andersc.tour.values

fun String.addEnthusiasm(n: Int = 1) = this + "!".repeat(n)

val String.numVowels
    get() = count { "aoeiu".contains(it) }

infix fun String?.showWithDefault(default: String) = print(this ?: default)

fun <T> T.show(): T {
    println(this)
    return this
}

fun main() {
    "hello".show().addEnthusiasm(3).show()
    "hello".numVowels.show()

    val nullableStr: String? = null
    nullableStr showWithDefault "default str"
}
