using System;
using System.Threading;
using System.Windows.Forms;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class MultiThreadsIssue
    {
        public static void Demo()
        {
            Console.WriteLine("***** Synchronizing Threads ***** \n");

            Console.WriteLine("primary thread [{0}] is executing.", Thread.CurrentThread.ManagedThreadId);

            // worker class
            var p = new Printer2();
            // make 10 threads
            var threads = new Thread[10];
            for (var i = 0; i < 10; i++)
            {
                threads[i] = new Thread(p.PrintNumbers);
                threads[i].Name = string.Format("Worker thread #{0}", i);
            }

            foreach (var thread in threads)
            {
                thread.Start();
            }

            Console.ReadLine();
        }
    }
}