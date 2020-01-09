using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChainDelegat
{
    class AccessHandler : Handler
    {
        public override void HandleRequest(string login, string password)
        {
            NewConsole.WriteLineGreen("ВХОД ВЫПОЛНЕН, ДОБРО ПОЖАЛОВАТЬ " + login);
        }
    }
}
