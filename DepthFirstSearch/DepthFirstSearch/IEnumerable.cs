using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DepthFirstSearch
{
    interface IEnumerable
    {
        IIterator GetIterator();
    }
}
