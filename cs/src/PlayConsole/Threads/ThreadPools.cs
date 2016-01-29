using System;
using System.Threading;
using System.Threading.Tasks;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class ThreadPools
    {
        public static void Demo()
        {
            Console.WriteLine("***** Fun with the CLR Thread Pool ***** \n");

            Console.WriteLine("primary thread [{0}] is executing.", Thread.CurrentThread.ManagedThreadId);

            var p = new Printer();
            var workItem = new WaitCallback(PrintTheNumbers);

            // Queue the method 10 times.
            var threads = new Thread[10];
            for (var i = 0; i < 10; i++)
            {
                ThreadPool.QueueUserWorkItem(workItem, p);
            }

            Console.WriteLine("All tasks queued.");
            Console.ReadLine();
        }

        private static void PrintTheNumbers(object state)
        {
            var task = state as Printer;
            task.PrintNumbers();
        }
    }
}