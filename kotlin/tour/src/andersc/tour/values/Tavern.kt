package andersc.tour.values

import java.io.File
import kotlin.math.roundToInt

const val TAVERN_NAME = "Taernyl's Folly"
private val firstNames = mutableListOf("Eli", "Mordoc", "Sophie")
private val lastNames = listOf("Ironfoot", "Fernsworth", "Baggins")
private val patrons = mutableSetOf<String>()
private val menus = File("data/menus.txt")
    .readText()
    .split("\n")
    .filter { it.isNotEmpty() }
//private var playerGold = 10
//private var playerSilver = 10
private val patronsGold = mutableMapOf<String, Double>()

fun main() {

    (0..9).forEach {
        val first = firstNames.shuffled().first()
        val last = lastNames.shuffled().first()
        patrons += "$first $last"
    }

    patrons.forEach { patronsGold[it] = 9.0 }

    // println(patronsGold)
    patrons.forEachIndexed { i, patron ->
        placeOrder(patron, menus.shuffled().first())
    }

    // println(patrons.first())
    // println(patrons.getOrElse(3) { "Unknown patron"})
    // println(patrons.getOrNull(4) ?: "Unknown patron")

    if (patrons.containsAll(listOf("Sophie", "Eli"))) {
        println("The tavern master says: Yea, they're seated by the stew kettle.")
    } else {
        println("The tavern master says: Nay, they departed hours ago.")
    }

//    patrons.run {
//        remove("Eli")
//        add("Alex")
//        add(0, "Bar")
//    }
//    patrons[0] = "Alexis"

//    sayGreetings(patrons)
}

fun sayGreetings(patrons: Collection<String>) {
//    for (p in patrons) {
//        println("Good evening, $p")
//    }
//    patrons.forEach { println("Good evening, $it")}
    patrons.forEachIndexed { i, p -> println("Good evening, $p - you're #${i+1} in line")}
}

fun placeOrder(patron: String, menu: String) {
    val i = TAVERN_NAME.indexOf('\'')
    // ext methods
    val tavernMaster = TAVERN_NAME.substring(0 until i)
    println("$patron speaks with $tavernMaster about their order.")

//    val menuItem = menu.split(',')
//    // index access operator
//    val type = menuItem[0]
//    val name = menuItem[1]
//    val price = menuItem[2]

    // destructuring: List, Map, Pair
    val (type, name, price) = menu.split(',')
    println("$patron buys a $name ($type) for $price.")

     performPurchase(patron, price.toDouble())

    val phrase = if (name == "Dragon's Breath") {
        "$patron exclaims: ${translateToDragonSpeak("Ah, delicious $name!")}"
    } else {
        "$patron says: Thanks for the $name"
    }
    println(phrase)

    displayBalance()

    // println(translateToDragonSpeak("IT'S GOT WHAT ADVENTURERS CRAVE"))
}

//fun performPurchase(price: Double) {
//    displayBalance()
//    val totalPurse = playerGold + playerSilver / 100.0
//    println("Total purse: $totalPurse")
//    println("Purchasing item for $price")
//
//    val remaining = totalPurse - price
//    println("Remaining balance: ${"%.2f".format(remaining)}")
//
//    val remainingGold = remaining.toInt()
//    val remainingSilver = ((remaining - remainingGold) * 100).roundToInt()
//    playerGold = remainingGold
//    playerSilver = remainingSilver
//    displayBalance()
//}

fun performPurchase(patron: String, price: Double) {
    val totalPurse = patronsGold.getValue(patron)
    patronsGold[patron] = totalPurse - price
}

fun displayBalance() {
    patronsGold.forEach { patron, balance ->
        println("$patron, balance: ${"%.2f".format(balance)}")
    }
}

fun translateToDragonSpeak(phrase: String) =
    phrase.replace(Regex("[aeiouAEIOU]")) { m ->
        when (m.value) {
            "a", "A" -> "4"
            "e", "E" -> "3"
            "i", "I" -> "1"
            "o", "O" -> "0"
            "u", "U" -> "|_|"
            else -> m.value
        }
    }
