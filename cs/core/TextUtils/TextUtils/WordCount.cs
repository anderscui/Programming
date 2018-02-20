using System;
using System.Linq;

namespace TextUtils
{
    public class WordCount
    {
        public static int GetWordCount(string search, string input)
        {
            if (string.IsNullOrEmpty(search) || string.IsNullOrEmpty(input))
            {
                return 0;
            }

            var source = input.Split(new char[] { '.', '?', '!', ' ', ';', ':', ',' });
            var matches = from word in source
                          where word.ToLowerInvariant() == search.ToLowerInvariant()
                          select word;
            return matches.Count();
        }
    }
}
