package andersc.tour.values

class Barrel<out T>(val item: T)

fun main() {
    var fedoraBarrel = Barrel(Fedora("fedora", 15))
    var lootBarrel: Barrel<Loot> = Barrel(Coin(15))

    lootBarrel = fedoraBarrel
    // smart cast is required.
    val fedora = lootBarrel.item
}
