val l1 = List("a", "b", "c")
val l2 = List(1, 2, 3)

val zipped = l1 zip l2
val zipped2 = zipped zip l2

val partitioned = l2 partition (i => i % 2 == 0)