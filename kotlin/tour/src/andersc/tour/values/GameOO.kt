package andersc.tour.values

import java.lang.Exception
import java.lang.IllegalStateException
import kotlin.system.exitProcess

fun main() {
    Game.play()
}

object Game {
    private val player = Player("Madrigal")

    private var worldMap = listOf(
        listOf(TownSquare(), Room("Tavern"), Room("Back Room")),
        listOf(Room("Long Corridor"), Room("Generic Room"))
    )
    private var curRoom = worldMap[0][0]

    init {
        println("Welcome, adventurer.")
        player.castFireball()
    }

    private fun move(directionInput: String) =
        try {
            val dir = Direction.valueOf(directionInput.toUpperCase())
            val newPos = dir.updateCoordinate(player.curPosition)
            if (!newPos.isInBounds) {
                throw IllegalStateException("$dir is out of bounds.")
            }
            val newRoom = worldMap[newPos.y][newPos.x]
            player.curPosition = newPos
            curRoom = newRoom

            "OK, you move $dir to the ${newRoom.name}.\n ${newRoom.load()}"
        } catch (e: Exception) {
            "Invalid direction: $directionInput."
        }

    private fun fight() = curRoom.monster?.let {
        while (player.healthPoints > 0 && it.healthPoints > 0) {
            slay(it)
            Thread.sleep(200)
        }

        "Combat complete"
    } ?: "There's nothing here to fight."

    private fun slay(monster: Monster) {
        println("${monster.name} did ${monster.attack(player)} damage!")
        println("${player.name} did ${player.attack(monster)} damage!")

        if (player.healthPoints <= 0) {
            println(">>> You have been defeated! Thanks for playing. <<<")
            exitProcess(0)
        }
        if (monster.healthPoints <= 0) {
            println(">>> ${monster.name} have been defeated! <<<")
            curRoom.monster = null
        }
    }

    fun play() {
        while (true) {
            println(curRoom.description())
            println(curRoom.load())

            showPlayerStatus(player)

            print("> Enter your command: ")
            val result = GameInput(readLine()).processCommand()
            if (result == "quit") {
                break
            } else {
                println(result)
            }
        }
    }

    private fun showPlayerStatus(player: Player) {
        println("${player.name} ${player.formatHealthStatus()}")
        println("(Aura: ${player.auraColor()}) (Blessed: ${if (player.isBlessed) "YES" else "NO"})")
    }

    private class GameInput(arg: String?) {
        private val input = arg ?: ""
        val command = input.split(" ")[0]
        val argument = input.split(" ").getOrElse(1) { "" }

        private fun commandNotFound() = "I'm not quite sure what you're trying to do."

        fun processCommand() = when (command.toLowerCase()) {
            "move" -> move(argument)
            "fight" -> fight()
            "quit", "exit", "q", "e" -> {
                println("bye")
                "quit"
            }
            else -> commandNotFound()
        }
    }
}

