using System;

namespace Hello
{
    class Program
    {
        static void Main(string[] args)
        {
            var generator = new FibonacciGenerator();
            foreach (var f in generator.Generate(15)) {
              Console.WriteLine(f);
            }
        }
    }
}
