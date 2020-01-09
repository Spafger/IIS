using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fabricmethod
{
    class LCarDeveloper : Developer
    {
        public LCarDeveloper(string n) : base(n)
        { }

        public override Cars Create()
        {
            return new LCar();
        }
    }
}
