using System;
using System.Runtime.Remoting.Messaging;
using System.Threading;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class AsyncDelegateCallback
    {
        public delegate int BinaryOp(int x, int y);

        private static bool IsDone = false;

        public static void Demo()
        {
            Console.WriteLine("***** Async Delegate Callback Demo *****");
            Console.WriteLine("Running on main thread [{0}].", Thread.CurrentThread.ManagedThreadId);

            BinaryOp op = Add;
            var iftAR = op.BeginInvoke(1, 2, AddCompleted, null);

            while (!IsDone)
            {
                Console.WriteLine("The async action's not done, so I can do something else in main thread.");
                Thread.Sleep(500);
            }
            Console.WriteLine("Yeah, it's done. Time to collect async data.");
            
            Console.ReadLine();
        }

        private static void AddCompleted(IAsyncResult ar)
        {
            Console.WriteLine("AddCompleted() invoded on thread [{0}].", Thread.CurrentThread.ManagedThreadId);
            Console.WriteLine("Your addition is complete:)");

            // Get the result
            var asyncResult = (AsyncResult)ar;
            var op = (BinaryOp) asyncResult.AsyncDelegate;
            Console.WriteLine("1 + 2 is {0}.", op.EndInvoke(ar));

            IsDone = true;
        }

        private static int Add(int x, int y)
        {
            Console.WriteLine("Add() invoked on thread [{0}].", Thread.CurrentThread.ManagedThreadId);
            Thread.Sleep(2000);

            return x + y;
        }
    }
}
