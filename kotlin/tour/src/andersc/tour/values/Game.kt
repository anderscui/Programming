package andersc.tour.values

fun main() {
    val name = "Madrigal"
    val healthPoints = 89
    val isBlessed = true
    val isImmortal = false

    val healthStatus = formatHealthStatus(healthPoints, isBlessed)
    val auraColor = auraColor(isBlessed, healthPoints, isImmortal)
    showPlayerStatus(name, healthStatus, auraColor, isBlessed)

    castFireball()

//    val race = "gnome"
//    val faction = when (race) {
//        "dwarf" -> "Keepers of the Mines"
//        "gnome" -> "Keepers of the Mines"
//        "orc" -> "Free People of the Rolling Hills"
//        "human" -> "Free People of the Rolling Hills"
//        else -> "unknown"
//    }
//    println(faction)
}

private fun castFireball(n: Int = 2) =
    println("A glass of Fireball springs into existence. (x$n)")

private fun showPlayerStatus(
    name: String,
    healthStatus: String,
    auraColor: String,
    isBlessed: Boolean
) {
    println("$name $healthStatus")
    println("(Aura: $auraColor) (Blessed: ${if (isBlessed) "YES" else "NO"})")
}

private fun auraColor(
    isBlessed: Boolean,
    healthPoints: Int,
    isImmortal: Boolean
): String {
    val auraVisible = isBlessed && healthPoints > 50 || isImmortal
    val auraColor = if (auraVisible) "Green" else "NONE"
    return auraColor
}

private fun formatHealthStatus(healthPoints: Int, isBlessed: Boolean): String {
    val healthStatus = if (healthPoints >= 100) {
        "is in excellent condition."
    } else if (healthPoints in 90..99) {
        "has a few scratches."
    } else if (healthPoints >= 75) {
        if (isBlessed) {
            "has some minor wounds but is healing quite quickly."
        } else {
            "has some minor wounds."
        }
    } else if (healthPoints >= 15) {
        "looks pretty hurt."
    } else {
        "is in awful condition."
    }
    return healthStatus
}
