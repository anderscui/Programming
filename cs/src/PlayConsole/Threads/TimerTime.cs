using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Andersc.CodePlay.PlayConsole.Threads
{
    public class TimerTime
    {
        private static void PrintTime(object state)
        {
            Console.WriteLine("Time is: {0}, state: {1}", 
                DateTime.Now.ToLongTimeString(), state);
        }

        public static void Demo()
        {
            Console.WriteLine("***** Working with Timer Type ***** \n");
            
            var timeCB = new TimerCallback(PrintTime);
            var t = new Timer(
                timeCB,
                "timer",
                0,
                1000);

            Console.WriteLine("Hit key to ternimate...");
            Console.ReadLine();
        }
    }
}
