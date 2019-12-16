package me.andersc.implicits

import me.andersc.Fraction

object implicitBoth {
  def smaller[T](a: T, b: T)(implicit order: T => Ordered[T]): T = if (a < b) a else b

  def main(args: Array[String]): Unit = {
    println(smaller(2, 1))
    println(smaller("hello", "world"))
    println(smaller(Fraction(2, 3), Fraction(3, 4)))
  }
}
