package me.andersc.implicits

import me.andersc._

object implicitConversion {
  def main(args: Array[String]): Unit = {
    implicit def int2Fraction(n: Int): Fraction = Fraction(n, 1)

    val left: Fraction = 3
    println(left)

    val result = 3 * Fraction(4, 5)
    println(result)
  }
}
