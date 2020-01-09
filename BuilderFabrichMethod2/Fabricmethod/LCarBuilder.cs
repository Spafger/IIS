using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fabricmethod
{
    class LCarBuilder : CarBuilder
    {
        
        public override void SetBody()
        {
           this.Parts.Body = new Body { Type = "Легковой кузов: " + LBodyMoney + " рублей" };
        }

        public override void SetBus()
        {
            this.Parts.Bus = new Bus { Type = "Легкие шины: " + LBusMoney + " рублей" };
        }

        public override void SetEngine()
        {
            this.Parts.Engine = new Engine { Type = "Легковой двигатель: " + LEngineMoney  + " рублей" };
        }

        public override void SetMoney()
        {
            this.Parts.Money = new Money { Sum = "Итого: " + (LBodyMoney + LBusMoney + LEngineMoney) + " рублей" };
        }
    }
}

