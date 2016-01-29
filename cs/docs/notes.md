

# Multithreading

A thread was defined as a path of execution within an executable application.

Using additional threads, you can build more responsive (not necessarily faster) apps.

The is not a direct one-to-one correspondence between app domains and threads.

Aborting or suspending an active thread is generally considered a bad idea.

Assignments and simple arithmetic operations are not **atomic**.

# The Problem of Concurrency

One of the many "painful aspects" of multithreaded programming is that you have little control
over how the underlying OS or the CLR uses its threads.

thread-volative vs. atomic

# Libs

delegate type, TPL(Task Parallel Library), async & await


# ThreadPool

Pooled threads are always background threads with default priority(Normal).