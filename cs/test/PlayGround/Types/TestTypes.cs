using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics.Contracts;
using NUnit.Framework;

namespace Andersc.CodePlay.PlayGround.Types
{
    [TestFixture]
    public class TestTypes
    {
        [Test]
        public void TestGetType()
        {
            var l = new ArrayList();
            var lt = l.GetType();
            Console.WriteLine("Type: {0}, Is abstract? {1}, Is sealed? {2}, Is generic? {3}",
                lt.Name, lt.IsAbstract, lt.IsSealed, lt.IsGenericType);
        }

        [Test]
        public void TestTypeOf()
        {
            var lt = typeof(List<int>);
            Console.WriteLine("Type: {0}, Is abstract? {1}, Is sealed? {2}, Is generic? {3}",
                lt.Name, lt.IsAbstract, lt.IsSealed, lt.IsGenericType);
        }

        [Test]
        public void TestStaticGetType()
        {
            var st = Type.GetType("System.String");
            Console.WriteLine("Type: {0}, Is abstract? {1}, Is sealed? {2}, Is generic? {3}",
                st.Name, st.IsAbstract, st.IsSealed, st.IsGenericType);

            //st = Type.GetType("System.String, System");
            //Console.WriteLine("Type: {0}, Is abstract? {1}, Is sealed? {2}, Is generic? {3}",
            //    st.Name, st.IsAbstract, st.IsSealed, st.IsGenericType);
        }
    }
}