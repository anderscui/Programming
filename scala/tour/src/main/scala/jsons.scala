import io.circe._
import io.circe.parser._
import io.circe.generic.auto._
import io.circe.syntax._

/**
  * Created by andersc on 4/24/17.
  */
object jsons {
  def main(args: Array[String]): Unit = {
    val json: String = """
    {
      "id": "c730433b-082c-4984-9d66-855c243266f0",
      "name": "Foo",
      "counts": [1, 2, 3],
      "values": {
        "bar": true,
        "baz": 100.001,
        "qux": ["a", "b"]
      }
    }
    """
//    val doc = parse(json).getOrElse(Json.Null).asInstanceOf[Map[String, Any]]
//    println(doc)

    val o = Map[String, Any]("a" -> 1, "b" -> 2, "c" -> Map("d" -> 1, "e" -> 2))
//    println(o.asJson.noSpaces)
  }
}
