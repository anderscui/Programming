using System;
using System.Threading;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class Printer
    {
        public void PrintNumbers()
        {
            Console.WriteLine("Thread [{0}] is executing PrintNumbers.", Thread.CurrentThread.ManagedThreadId);

            for (int i = 0; i < 10; i++)
            {
                Console.Write("{0}, ", i);
                Thread.Sleep(300);
            }

            Console.WriteLine();
        }
    }
}