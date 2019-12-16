package me.andersc

import scala.math._

class Fraction(n: Int, d: Int) extends Ordered[Fraction] {
  private val num: Int = if (d == 0) 1 else n * sign(d) / gcd(n, d)
  private val den: Int = if (d == 0) 0 else d * sign(d) / gcd(n, d)
  override def toString: String = num + "/" + den

  def sign(a: Int): Int = if (a > 0) 1 else if (a > 0) -1 else 0
  def gcd(a: Int, b: Int): Int = if (b == 0) abs(a) else gcd(b, a % b)

  def *(other: Fraction) = new Fraction(num * other.num, den * other.den)

  override def compare(that: Fraction): Int = {
    (this.num*that.den).compare(that.num*this.den)
  }
}

object Fraction {
  def apply(n: Int, d: Int): Fraction = new Fraction(n, d)
}
