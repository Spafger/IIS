using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChainDelegat
{
	internal class Program
	{
        public static void Main()
        {
            
            Handler h1 = new LoginHandler();
            Handler h2 = new PasswordHandler();
            Handler h3 = new AccessHandler();


            h1.SetSuccessor(h2);
            h2.SetSuccessor(h3);

            Console.WriteLine("Добро пожаловать в систему, подтвердите ваши данные.");
            Console.Write("Введите логин: ");
            string login = Console.ReadLine(); 
            Console.Write("Введите пароль: ");
            string password = Console.ReadLine();

            h1.HandleRequest(login, password);

            NewConsole.ReadLine();
        }
    }
}