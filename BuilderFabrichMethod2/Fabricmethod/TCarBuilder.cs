using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fabricmethod
{
    class TCarBuilder : CarBuilder
    {
        
        public override void SetBody()
        {
            this.Parts.Body = new Body { Type = "Грузовой кузов: " + TBodyMoney + " рублей" };
        }

        public override void SetBus()
        {
            this.Parts.Bus = new Bus { Type = "Тяжелые шины: " + TBusMoney + " рублей" };
        }

        public override void SetEngine()
        {
            this.Parts.Engine = new Engine { Type = "Грузовой двигатель: " + TEngineMoney + " рублей" };
        }

        public override void SetMoney()
        {
            this.Parts.Money = new Money { Sum = "Итого: " + (TBodyMoney + TBusMoney + TEngineMoney) + " рублей" };
        }
    }
}
