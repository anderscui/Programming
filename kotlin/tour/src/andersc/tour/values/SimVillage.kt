package andersc.tour.values

fun main() {
    runSim()
}

//fun runSim(player: String, costPrinter: (Int) -> Unit, greeter: (String, Int) -> String) {
//    val numBuildings = (1..3).random()
//    costPrinter(numBuildings)
//    println(greeter(player, numBuildings))
//}

fun runSim() {
    val greetingFunc = configGreeting()
    println(greetingFunc("Guyal"))
}

fun showConstructionCost(numBuildings: Int) {
    val cost = 500
    println("construction cost: ${cost * numBuildings}")
}

fun configGreeting(): (String) -> String {
    val structType = "schools"
    val numBuildings = 5
    return { player: String ->
        val curYear = 2019
        println("Adding $numBuildings houses of $structType.")
        showConstructionCost(numBuildings)
        "Welcome to SimVillage, $player! (copyright $curYear)"
    }
}
