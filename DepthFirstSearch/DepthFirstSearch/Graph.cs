using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DepthFirstSearch
{
    class Graph : IEnumerable
    {

        public Dictionary<int, HashSet<int>> Node { get; private set; }

        public Graph()
        {
            Node = new Dictionary<int, HashSet<int>>();
        }


        public IIterator GetIterator()
        {
            return new GraphNumerator(Node);
        }

        public void AddEdge(int source, int target)
        {
            if (Node.ContainsKey(source))
            {
                try
                {
                    Node[source].Add(target);
                }
                catch
                {
                    Console.WriteLine("This edge already exists: " + source + " to " + target);
                }
            }
            else
            {
                var hs = new HashSet<int>();
                hs.Add(target);
                Node.Add(source, hs);
            }
        }
    }
}
