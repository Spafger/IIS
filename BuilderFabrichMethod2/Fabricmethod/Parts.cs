using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fabricmethod
{
    class Parts
    {
        public Body Body { get; set; }
        
        public Bus Bus { get; set; }
       
        public Engine Engine { get; set; }

        public Money Money { get; set; }

        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();

            if (Body != null)
                sb.Append(Body.Type + "\n");
            if (Bus != null)
                sb.Append(Bus.Type + "\n");
            if (Engine != null)
                sb.Append(Engine.Type + "\n");
            if (Money != null)
                sb.Append(Money.Sum + " \n");
            return sb.ToString();
        }
    }
}
