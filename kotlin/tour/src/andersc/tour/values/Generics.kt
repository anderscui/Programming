package andersc.tour.values

class LootBox<T: Loot>(vararg item: T) {
    var open = false

    private var loot: Array<out T> = item

    operator fun get(index: Int): T? = loot[index].takeIf { open }

    fun fetch(i: Int): T? {
        return loot[i].takeIf { open }
    }

    fun <R> fetch(i: Int, lootModFunc: (T) -> R): R? {
        return lootModFunc(loot[i]).takeIf { open }
    }
}

open class Loot(val value: Int)

class Fedora(val name: String, value: Int): Loot(value)

class Coin(value: Int): Loot(value)

fun main() {
    val lootBox = LootBox(
        Fedora("fedora", 15),
        Fedora("vedora", 25))
    val lootBox2 = LootBox(Coin(15))

    lootBox.open = true
    lootBox[1]?.run { println("You retrieved $name from the box") }

    lootBox2.open = true
    val coin = lootBox2.fetch(0) {
        Coin(it.value * 3)
    }
    coin?.let { println(it.value) }
}
