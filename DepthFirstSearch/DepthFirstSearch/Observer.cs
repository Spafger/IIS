using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DepthFirstSearch
{
    class Observer : IObserver
    {
        public string Name { get; private set; }

        public Observer(string name)
        {
            Name = name;
        }


        public void Update(IObserver observer, int i)
        {
            Console.WriteLine("{0} получил значение: {1}.", observer.Name, i);
        }
    }
}
