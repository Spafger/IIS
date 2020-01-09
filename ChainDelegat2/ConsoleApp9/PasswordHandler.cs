using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChainDelegat
{
    class PasswordHandler : Handler
    {
        public override void HandleRequest(string login, string password)
        {
            if (passwords.Contains(password))
            {
                successor.HandleRequest(login, password);
            }
            else
            {
                NewConsole.WriteLineRed("ВХОД ЗАПРЕЩЕН, НЕВЕРНЫЙ ПАРОЛЬ");
            }
        }
    }
}
