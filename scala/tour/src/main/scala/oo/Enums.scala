package oo

/**
  * Created by andersc on 5/14/17.
  */
object WeekDay extends Enumeration {
  type WeekDay = Value

  val Mon, Tue, Wed, Thu, Fri, Sat, Sun = Value
}

object TestEnums {
  import WeekDay._

  def isWorkingDay(d: WeekDay) = {
    ! (d == Sat || d == Sun)
  }

  def main(args: Array[String]): Unit = {
    WeekDay.values foreach (d => println(d.toString))
  }
}