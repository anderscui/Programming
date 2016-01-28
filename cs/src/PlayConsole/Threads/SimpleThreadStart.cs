using System;
using System.Threading;
using System.Windows.Forms;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class SimpleThreadStart
    {
        public static void Demo()
        {
            Console.WriteLine("***** The Amazing Thread App ***** \n");
            Console.WriteLine("Do you want [1] or [2] threads? ");

            var count = Console.ReadLine();

            Console.WriteLine("primary thread [{0}] is executing.", Thread.CurrentThread.ManagedThreadId);

            // worker class
            var p = new Printer();
            switch (count)
            {
                case "2":
                    //var backgroundThread = new Thread(p.PrintNumbers);
                    var backgroundThread = new Thread(new ThreadStart(p.PrintNumbers));
                    backgroundThread.Name = "Secondary";
                    backgroundThread.Start();
                    break;
                case "1":
                    p.PrintNumbers();
                    break;
                default:
                    Console.WriteLine("WTF do you want... you get 1 thread.");
                    goto case "1";
            }

            // some additional work
            MessageBox.Show("I'm busy!", "Work on primary thread...");
            Console.ReadLine();
        }
    }
}