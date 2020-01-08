using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DepthFirstSearch
{
    interface IIterator
    {
        void Next();

        void Attach(IObserver observer);
    }
}
