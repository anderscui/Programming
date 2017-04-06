def safeTrim(s: String): String = {
  if (s == null)
    return null
  s.trim
}

def log(d: Double) = println(f"Got value $d%.2f")
log(3.1415)

// deprecated syntax
def log2(d: Double) { println(f"Got value $d%.2f") }

// empty parentheses
def hi(): String = "hi"
