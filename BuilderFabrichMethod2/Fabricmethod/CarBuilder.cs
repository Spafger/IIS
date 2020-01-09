using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fabricmethod
{
    abstract class CarBuilder
    {
        public Parts Parts { get; private set; }
        public void CreateParts()
        {
            Parts = new Parts();
        }
        public abstract void SetBody();
        public abstract void SetBus();
        public abstract void SetEngine();
        public abstract void SetMoney();

        public int TBodyMoney = 25000;
        public int TBusMoney = 15000;
        public int TEngineMoney = 35000;

        public int LBodyMoney = 20000;
        public int LBusMoney = 10000;
        public int LEngineMoney = 30000;

    }
}

