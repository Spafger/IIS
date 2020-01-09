using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChainDelegat
{
    class LoginHandler : Handler
    {
        public override void HandleRequest(string login, string password)
        {
            if (logins.Contains(login))
            {
                successor.HandleRequest(login, password);
            }
            else
            {
                NewConsole.WriteLineRed("ВХОД ЗАПРЕЩЕН, НЕВЕРНЫЙ ЛОГИН");
            }
        }
    }
}
