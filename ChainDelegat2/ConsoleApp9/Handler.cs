using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChainDelegat
{
    abstract class Handler
    {
        protected Handler successor;

        public void SetSuccessor(Handler successor)
        {
            this.successor = successor;
        }

        public string[] passwords = new string[] { "12346584", "278954", "3548864", "123456", "54568465", "754868", "8888" };
        public string[] logins = new string[] { "job", "robokop", "lol", "car", "red", "igor" };

        public abstract void HandleRequest(string login, string password);
    }
}
