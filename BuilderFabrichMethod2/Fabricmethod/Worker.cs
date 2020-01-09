using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fabricmethod
{
    class Worker
    {
        public Parts Make(CarBuilder carBuilder)
        {
            carBuilder.CreateParts();
            carBuilder.SetBody();
            carBuilder.SetBus();
            carBuilder.SetEngine();
            carBuilder.SetMoney();
            return carBuilder.Parts;
        }
    }
}
