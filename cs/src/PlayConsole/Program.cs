using System;
using System.Threading;
using Andersc.CodePlay.PlayConsole.Threads;

namespace Andersc.CodePlay.PlayConsole
{
    class Program
    {
        public delegate int BinaryOp(int x, int y);

        static void Main(string[] args)
        {
            //ThreadStats();

            // Use Async Delegates
            //SyncDelegate.Demo();
            //AsyncDelegate.Demo();
            //AsyncDelegateCallback.Demo();
            //AsyncDelegateStateData.Demo();

            // Use Thread Type
            //SimpleThreadStart.Demo();
            ParameterizedThreadStarts.Demo();
        }

        static void ThreadStats()
        {
            Console.WriteLine("***** Primary Thread Stats *****\n");
            var curThread = Thread.CurrentThread;
            curThread.Name = "PrimaryThread";

            var appDomain = Thread.GetDomain();
            Console.WriteLine("AppDomain: " + appDomain.FriendlyName);

            var ctx = Thread.CurrentContext;
            Console.WriteLine("Context ID: " + ctx.ContextID);

            Console.WriteLine("Thread Name: " + curThread.Name);
            Console.WriteLine("Thread IsAlive: " + curThread.IsAlive);
            Console.WriteLine("Thread Priority: " + curThread.Priority);
            Console.WriteLine("Thread ThreadState: " + curThread.ThreadState);

            Console.ReadLine();
        }
    }
}
