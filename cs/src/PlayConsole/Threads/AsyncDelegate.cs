using System;
using System.Threading;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class AsyncDelegate
    {
        public delegate int BinaryOp(int x, int y);

        public static void Demo()
        {
            Console.WriteLine("***** Async Delegate Demo *****");
            Console.WriteLine("Running on main thread [{0}].", Thread.CurrentThread.ManagedThreadId);

            BinaryOp op = Add;
            var iftAR = op.BeginInvoke(1, 2, null, null);

            while (!iftAR.IsCompleted)
            {
                Console.WriteLine("The async action's not done, so I can do something else in main thread.");
                Thread.Sleep(500);
            }
            
            Console.WriteLine("Yeah, it's done. Time to collect async data.");

            var ans = op.EndInvoke(iftAR);
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
