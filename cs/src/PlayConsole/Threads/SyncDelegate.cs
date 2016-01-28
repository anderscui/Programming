using System;
using System.Threading;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class SyncDelegate
    {
        public delegate int BinaryOp(int x, int y);

        public static void Demo()
        {
            Console.WriteLine("***** Sync Delegate Demo *****");
            Console.WriteLine("Running on main thread [{0}].", Thread.CurrentThread.ManagedThreadId);

            BinaryOp op = Add;
            var ans = op(1, 2);

            Console.WriteLine("Doing something else in main thread.");
            Console.WriteLine("1 + 2 is {0}.", ans);
            Console.ReadLine();
        }

        private static int Add(int x, int y)
        {
            Console.WriteLine("Add() invoked on thread [{0}].", Thread.CurrentThread.ManagedThreadId);
            Thread.Sleep(2000);

            return x + y;
        }
    }
}
