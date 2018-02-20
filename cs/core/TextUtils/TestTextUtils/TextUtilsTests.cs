using Xunit;
using TextUtils;
using System.Diagnostics;

namespace TestTextUtils
{
    public class GetWordCountShould
    {
        [Fact]
        public void IgnoreCasing()
        {
            var wc = WordCount.GetWordCount("Jack", "Jack jack");
            Assert.Equal(2, wc);
        }

        [Theory]
        [InlineData(0, "Ting", "Does not appear in the string.")]
        [InlineData(1, "Ting", "Ting appears once.")]
        [InlineData(2, "Ting", "Ting appears twice with Ting.")]
        public void CountInstancesCorrectly(int count,
                                    string search,
                                    string input)
        {
            Assert.Equal(count, WordCount.GetWordCount(search, input));
        }
    }
}
