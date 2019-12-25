package andersc.tour.values.extensions

fun <T> Iterable<T>.random(): T = this.shuffled().first()
