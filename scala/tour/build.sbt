name := "tour"

version := "1.0"

scalaVersion := "2.12.1"


libraryDependencies += "org.scala-lang.modules" %% "scala-parser-combinators" % "1.0.5"


val circeVersion = "0.7.1"
libraryDependencies ++= Seq(
  "io.circe" %% "circe-core",
  "io.circe" %% "circe-generic",
  "io.circe" %% "circe-parser"
).map(_ % circeVersion)
