package fp

/**
  * Created by andersc on 10/05/2017.
  */
class Rational(n: Int, d: Int) {
  require(d != 0)

  private val g = gcd(n.abs, d.abs)
  val number: Int = n / g
  val denom: Int = d / g

  // auxiliary ctor
  def this(n: Int) = this(n, 1)

  def + (that: Rational): Rational = {
    new Rational(
      number * that.denom + that.number * denom,
      denom * that.denom
    )
  }

  def * (that: Rational): Rational = {
    new Rational(
      number * that.number,
      denom * that.denom
    )
  }

  override def toString: String = s"$number/$denom"

  private def gcd(a: Int, b: Int): Int =
    if (b == 0) a else gcd(b, a % b)
}

object TestRational {
  def main(args: Array[String]): Unit = {
    val r1 = new Rational(36, 42)
    println(r1)
    val r2 = new Rational(1, 3)
    println(r2)
    println(r1 + r2)
    println(r1 * r2)
  }
}
