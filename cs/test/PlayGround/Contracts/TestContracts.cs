using System;
using System.Collections;
using System.Diagnostics.Contracts;
using System.Linq;
using NUnit.Framework;

namespace Andersc.CodePlay.PlayGround.Contracts
{
    [TestFixture]
    public class TestContracts
    {
        private int Get(string s)
        {
            Contract.Assume(s != null);
            return 0;
        }

        [Test]
        public void TestGet()
        {
            var i = Get(null);
            Console.WriteLine(i);
        }
    }
}