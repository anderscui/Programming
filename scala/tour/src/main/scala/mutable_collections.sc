// ** mutable
val m = Map("AAPL" -> 597, "MSFT" -> 40)
val n = m - "AAPL" + ("GOOG" -> 521)

val nums = collection.mutable.Buffer(1)
for (i <- 2 to 10) nums += i
nums
nums.toList

val b = n.toBuffer
b += ("GOOG" -> 521)
b.toSet

