# The Java Memory Model

**A language memory model** is a spec that describes the circumstances under which a write to a var becomes visible to other threads.

The natural and simple model is **sequential consistency**. Sequential consistency has little to do with how processors and compilers really work.

A memory model is a trade-off between the predictable behavior of a concurrent program and a compiler's ability to perform optimizations. Not every language or platform has a memory model. **A typical purely functional programming language, which doesn't support mutations, does not need a memory model at all**.

Scala inherits its memory model from the JVM, which precisely specifies a set of happens-before relationships between diff actions in a program.

## happens-before actions in JVM

* Program order (sequence)
* Monitor locking (unlocking -> locking)
* Volatile fields (writing -> reading)
* Thread start (start() first)
* Thread termination
* Transitivity (A -> B, B -> C => A -> C)

## Immutable objects and final fields

We have said that programs must establish happends-before relationships to avoid data races, but there is an exception to this rule. If an object contains only **final fields** and the reference to the enclosing object does not become visible to another thread before the constructor completes, then the object is considered immutable and can be shared between the threads with any sync.

In Java, it's `final` keyword.


