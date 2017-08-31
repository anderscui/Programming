import scala.collection.mutable

val nums = (1 to 10).toList
val grouped = nums.groupBy(_ % 3)
for ((k, v) <- grouped) {
  println(k)
  println(v)
}

case class op(schema: String, table: String, action: String)

val ops = List(op("s1", "t1", "ins"), op("s1", "t1", "ins"), op("s1", "t1", "ins"),
  op("s2", "t2", "ins"), op("s1", "t1", "ins"), op("s1", "t1", "ins"),
  op("s2", "t2", "del"), op("s1", "t1", "upd"), op("s1", "t1", "upd"),
  op("s2", "t2", "ins"), op("s3", "t1", "ins"))

val gops = ops.groupBy(o => (o.schema, o.table, o.action))
assert(gops.size == 5)
for ((k, sops) <- gops) {
  println(k)
}

def getKey(o: op) = {
  (o.schema, o.table, o.action)
}

def shouldTake(x: op, y: op) = {
  getKey(x) == getKey(y)
}

def split(ops: List[op]): List[List[op]] = ops match {
  case Nil => Nil
  case h::t => {
    val segment = ops takeWhile { o => shouldTake(h, o)}
    segment :: split(ops drop segment.length)
  }
}

def group(ops: List[op]) = {

  var result: List[List[op]] = List.empty
  var curKey: (String, String, String) = ("", "", "")
  var curGroup: mutable.Buffer[op] = mutable.Buffer.empty

  for (o <- ops) {
    val k = getKey(o)
    if (k != curKey) {
      if (curGroup.nonEmpty) {
        result = curGroup.toList :: result
      }

      curKey = k
      curGroup = mutable.Buffer()
    }
    curGroup.append(o)
  }

  if (curGroup.nonEmpty) {
    result = curGroup.toList :: result
  }

  result.reverse
}

val results = group(ops)
for (sub_ops <- results) {
  println(sub_ops)
}

val results2 = split(ops)
for (sub_ops <- results2) {
  println(sub_ops)
}

