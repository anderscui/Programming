package oo

import apple.laf.JRSUIConstants.Widget

/**
  * Created by andersc on 11/05/2017.
  */
abstract class Element {
  import Element.elem

  def contents: Array[String]
  def height: Int = contents.length
  def width: Int = if (contents.isEmpty) 0 else contents(0).length

  def above(that: Element): Element = {
    val this1 = this widen that.width
    val that1 = that widen this.width
    elem(this.contents ++ that.contents)
  }

  def beside(that: Element): Element = {
    val this1 = this heighten that.height
    val that1 = that heighten this.height
    val contents = for ((line1, line2) <- this.contents zip that.contents)
                     yield line1 + line2
    elem(contents)
  }

  def widen(w: Int): Element = {
    if (w <= width) {
      this
    } else {
      val left = elem(' ', (w - width) / 2, height)
      val right = elem(' ', w - width - left.width, height)
      left beside this beside right
    }
  }

  def heighten(h: Int): Element = {
    if (h <= height) {
      this
    } else {
      val top = elem(' ', width, (h - height) / 2)
      val bot = elem(' ', width, h - height - top.height)
      top above this above bot
    }
  }

  override def toString: String = contents mkString "\n"
}

object Element {

  // val => create a field implicitly
  // contents => a field could implement an abstract method in super class.
  class ArrayElement(val contents: Array[String]) extends Element {
  }

  class LineElement(s: String) extends Element {
    val contents = Array(s)
    override def height: Int = 1
    override def width: Int = s.length
  }

  class UniformElement(
                        ch: Char,
                        override val width: Int,
                        override val height: Int) extends Element {
    private val line = ch.toString * width
    def contents: Array[String] = Array.fill(height)(line)
  }

  def elem(contents: Array[String]): Element =
    new ArrayElement(contents)

  def elem(ch: Char, width: Int, height: Int): Element =
    new UniformElement(ch, width, height)

  def elem(line: String): Element =
    new LineElement(line)
}
