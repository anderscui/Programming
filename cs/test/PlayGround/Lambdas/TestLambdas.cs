using System;
using System.Collections.Generic;
using NUnit.Framework;

namespace Andersc.CodePlay.PlayGround.Lambdas
{
    [TestFixture]
    public class TestLambdas
    {
        private bool IsOdd(int i)
        {
            return i%2 != 0;
        }

        [Test]
        public void TestAsParameter()
        {
            var list = new List<int>() {5, 2, 1, 6, 9};
            var odds = list.FindAll(new Predicate<int>(IsOdd));
            foreach (var odd in odds)
            {
                Console.Write("{0} ", odd);
            }

            odds = list.FindAll(IsOdd);
            CollectionAssert.AreEqual(odds, new []{5, 1, 9});

            odds = list.FindAll(delegate(int i)
            {
                return i%2 != 0;
            });
            CollectionAssert.AreEqual(odds, new[] {5, 1, 9});

            odds = list.FindAll(i => i%2 != 0);
            CollectionAssert.AreEqual(odds, new[] { 5, 1, 9 });
        }
    }
}