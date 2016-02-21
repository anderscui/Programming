using System;
using System.Collections;
using System.Diagnostics.Contracts;
using System.Linq;
using NUnit.Framework;

namespace Andersc.CodePlay.PlayGround.Lambdas
{
    [TestFixture]
    public class TestQueries
    {
        private int Get(string s)
        {
            Contract.Assume(s != null);

            return 0;
        }

        [Test]
        public void TestNongenericCollections()
        {
            var list = new ArrayList() { 5, 7, 3, 1, 9 };
            var lessThan5 = from i in list.OfType<int>()
                            where i < 5
                            select i;
            foreach (var i in lessThan5)
            {
                Console.WriteLine(i);
            }
        }
    }
}