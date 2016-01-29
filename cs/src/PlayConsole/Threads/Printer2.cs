using System;
using System.Threading;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class Printer2
    {
        private object threadLock = new object();

        public void PrintNumbers()
        {
            lock (threadLock)
            {
                Console.WriteLine("Thread [{0}] is executing PrintNumbers.", Thread.CurrentThread.ManagedThreadId);

                for (int i = 0; i < 10; i++)
                {
                    var random = new Random();
                    Thread.Sleep(300 * random.Next(5));
                    Console.Write("{0}, ", i);
                }

                Console.WriteLine();
            }
        }
    }
}