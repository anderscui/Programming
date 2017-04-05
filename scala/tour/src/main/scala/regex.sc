val input = "Enjoying this apple 3.14 times today"
val pat = """.* apple ([\d.]+) times .*""".r
val pat(amoutText) = input
val amout = amoutText.toDouble
