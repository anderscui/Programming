using System;
using TextUtils;

namespace WordCounter
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a search word:");
            var search = Console.ReadLine();
            Console.WriteLine("Provide a string to search:");
            var input = Console.ReadLine();

            var wc = WordCount.GetWordCount(search, input);
            var pluralChar = wc > 1 ? "s" : string.Empty;
            Console.WriteLine($"The search word {search} appears " +
                              $"{wc} time{pluralChar}.");
        }
    }
}
