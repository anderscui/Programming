def echo(args: String*) = {
  println(args.getClass)
  for (arg <- args)
    print(arg)
  println()
}

echo("Hello", ", ", "World!")

val params = List("Learning", " Scala")
// pass each item in a collection to the func.
echo(params: _*)
