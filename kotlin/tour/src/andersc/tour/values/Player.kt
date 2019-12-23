package andersc.tour.values

import java.io.File

class Player(name: String,
             var healthPoints: Int = 100,
             val isBlessed: Boolean,
             private val isImmortal: Boolean) {

    constructor(name: String) : this(name, isBlessed = true, isImmortal = false) {
        if (name.toLowerCase() == "kar") {
            healthPoints = 40
        }
    }

    // before calling ctors.
    init {
        require(healthPoints > 0) { "healthPoints must be positive."}
        require(name.isNotBlank()) { "Player must have a name."}
    }

    val hometown: String = selectHometown()

    private fun selectHometown(): String =
        File("data/towns.txt")
            .readText()
            .split("\n")
            .first { it.isNotEmpty() }

    var name = "madrigal"
        get() = "${field.capitalize()} of $hometown"
        private set(value) { field = value.trim() }

    fun castFireball(numFireballs: Int = 2) =
        println("A glass of Fireball springs into existence. (x$numFireballs)")

    fun formatHealthStatus(): String {
        val healthStatus = if (healthPoints >= 100) {
            "is in excellent condition."
        } else if (this. healthPoints in 90..99) {
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

    fun auraColor(): String {
        val auraVisible = isBlessed && healthPoints > 50 || isImmortal
        val auraColor = if (auraVisible) "Green" else "NONE"
        return auraColor
    }
}
