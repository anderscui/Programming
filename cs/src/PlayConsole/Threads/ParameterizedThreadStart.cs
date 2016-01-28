using System;
using System.Threading;
using System.Windows.Forms;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class ParameterizedThreadStarts
    {
        // signify that you haven't yet been notified.
        private static AutoResetEvent waitHandle = new AutoResetEvent(false);

        public class AddParams
        {
            public int X { get; set; }
            public int Y { get; set; }

            public AddParams(int x, int y)
            {
                X = x;
                Y = y;
            }
        }

        public static void Add(object data)
        {
            if (data is AddParams)
            {
                Console.WriteLine("Adding numbers in [{0}]", Thread.CurrentThread.ManagedThreadId);

                var ps = data as AddParams;
                Console.WriteLine("{0} + {1} is {2}.", ps.X, ps.Y, ps.X + ps.Y);

                // Tell other threads we are done.
                waitHandle.Set();
            }
        }

        public static void Demo()
        {
            Console.WriteLine("***** The Adding with Thread Objects ***** \n");
            Console.WriteLine("primary thread [{0}] is executing.", Thread.CurrentThread.ManagedThreadId);

            var ap = new AddParams(1, 2);
            var thread = new Thread(new ParameterizedThreadStart(Add));
            thread.Start(ap);

            // waiting
            //Thread.Sleep(5);

            // better waiting
            waitHandle.WaitOne();

            Console.ReadLine();
        }
    }
}