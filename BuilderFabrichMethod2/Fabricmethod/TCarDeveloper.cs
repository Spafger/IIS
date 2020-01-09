using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fabricmethod
{
    class TCarDeveloper : Developer
    {
        public TCarDeveloper(string n) : base(n)
        { }

        public override Cars Create()
        {
            return new TCar();
        }
    }
}
