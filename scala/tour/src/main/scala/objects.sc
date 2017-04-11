// Companion objects
class Multiplier(val x: Int) { def product(y: Int) = x * y }

object Multiplier {
  def apply(x: Int) = new Multiplier(x)
}

val tripe = Multiplier(3)
tripe.product(10)

// Access controls
object DBConn {
  private val db_url = "jdbc://localhost"
  private val db_user = "franken"
  private val db_pass = "berry"

  def apply() = new DBConn
}
class DBConn {
  private val props = Map(
    "url" -> DBConn.db_url,
    "user" -> DBConn.db_user,
    "pass" -> DBConn.db_pass
  )
  println(s"Created new conn for " + props("url"))
}

val conn = DBConn
