scalaVersion := "2.12.1"

name := "tour"
version := "1.0"
organization := "com.andersc"

//mainClass in assembly := Some("")

libraryDependencies += "org.scalatest" %% "scalatest" % "3.0.1" % "test"
libraryDependencies += "org.scala-lang.modules" %% "scala-async" % "0.9.6"

libraryDependencies += "ch.qos.logback" % "logback-classic" % "1.1.7"
libraryDependencies += "com.typesafe.scala-logging" %% "scala-logging" % "3.5.0"