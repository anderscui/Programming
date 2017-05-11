var assertionEnabled = true

def myAssert(predicate: => Boolean) = {
  if (assertionEnabled && !predicate) {
    throw new AssertionError
  }
}

// a func value is created for '5 > 3'
// which is evaluated when it's called
// i.e. when assertionEnabled is false, it's not called.
myAssert(5 > 3)

assertionEnabled = false
myAssert(1/0 == 0)