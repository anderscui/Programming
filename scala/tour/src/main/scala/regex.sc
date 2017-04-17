import scala.util.matching.Regex

val input = "Enjoying this apple 3.14 times today"
val pat = """.* apple ([\d.]+) times .*""".r
val pat(amoutText) = input
val amout = amoutText.toDouble

// replace
val pat2 = "(S|s)cala".r
pat2 replaceAllIn("Scala is scalable and cool?", "Java")
pat2 findAllIn("Scala is scalable and cool?") size


val st = """CREATE SEQUENCE candidate_id_seq
            START WITH 1
            INCREMENT BY 1
            NO MINVALUE
            NO MAXVALUE
            CACHE 1;"""

val RE_CS: Regex = "CREATE SEQUENCE".r
RE_CS.replaceAllIn(st, "")
