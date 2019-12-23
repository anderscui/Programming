package andersc.tour.values

fun main() {
    Game.play()
}

object Game {
    private val player = Player("Madrigal")
    private val curRoom: Room = TownSquare()

    init {
        println("Welcome, adventurer.")
        player.castFireball()
    }

    fun play() {
        while (true) {
            println(curRoom.description())
            println(curRoom.load())

            showPlayerStatus(player)

            print("> Enter your command: ")
            println("Last command: ${readLine()}")
        }
    }

    private fun showPlayerStatus(player: Player) {
        println("${player.name} ${player.formatHealthStatus()}")
        println("(Aura: ${player.auraColor()}) (Blessed: ${if (player.isBlessed) "YES" else "NO"})")
    }
}

