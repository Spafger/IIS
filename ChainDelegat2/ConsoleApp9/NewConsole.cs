using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChainDelegat
{
    internal class NewConsole
    {
        internal static void ReadLine()
        {
            Console.ReadLine();
        }

        internal static void WriteLineRed(string str)
        {
            var f = Console.ForegroundColor;
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(str);
            Console.ForegroundColor = f;
        }
        internal static void WriteLineGreen(string str)
        {
            var f = Console.ForegroundColor;
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine(str);
            Console.ForegroundColor = f;
        }
    }
}
