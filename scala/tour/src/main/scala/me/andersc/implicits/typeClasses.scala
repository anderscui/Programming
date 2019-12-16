package me.andersc.implicits

trait NumberLike[T] {
  def plus(x: T, y: T): T
  def divideBy(x: T, n: Int): T
}

object NumberLike {
  implicit object NumberLikeDouble extends NumberLike[Double] {
    override def plus(x: Double, y: Double): Double = x + y
    override def divideBy(x: Double, n: Int): Double = x / n
  }

  implicit object NumberLikeBigDecimal extends NumberLike[BigDecimal] {
    override def plus(x: BigDecimal, y: BigDecimal): BigDecimal = x + y
    override def divideBy(x: BigDecimal, n: Int): BigDecimal = x / n
  }
}

object typeClasses {
  import NumberLike.NumberLikeDouble

  def avg[T](x: T, y: T)(implicit ev: NumberLike[T]): T = {
    ev.divideBy(ev.plus(x, y), 2)
  }

  def avg2[T: NumberLike](x: T, y: T): T = {
    val ev = implicitly[NumberLike[T]]
    ev.divideBy(ev.plus(x, y), 2)
  }

  def main(args: Array[String]): Unit = {
    println(avg(1.0, 2))
    println(avg2(BigDecimal(1), BigDecimal(2)))
  }
}
