using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fabricmethod
{
    class Program
    {
        static void Main(string[] args)
        {
            Developer dev = new LCarDeveloper("ООО МашинСтрой");
            Console.WriteLine("Завод: " + dev.Name);
            Cars car1 = dev.Create();
            Worker worker = new Worker();
            CarBuilder builder = new LCarBuilder();
            Parts LParts = worker.Make(builder);
            Console.WriteLine(LParts.ToString());

            dev = new TCarDeveloper("ООО Рога и машины");
            Console.WriteLine("Завод: " + dev.Name);
            Cars car2 = dev.Create();
            builder = new TCarBuilder();
            Parts TParts = worker.Make(builder);
            Console.WriteLine(TParts.ToString());

            Console.ReadLine();
        }
    }
}
