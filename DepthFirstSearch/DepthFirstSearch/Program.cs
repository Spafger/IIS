using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DepthFirstSearch
{
    class Program
    {
        static void Main(string[] args)
        {
            Graph graph = new Graph();
            graph.AddEdge(1, 2);
            graph.AddEdge(1, 3);
            graph.AddEdge(1, 4);

            graph.AddEdge(2, 5);
            graph.AddEdge(2, 6);
            graph.AddEdge(4, 7);
            graph.AddEdge(4, 8);

            graph.AddEdge(5, 9);
            graph.AddEdge(5, 10);
            graph.AddEdge(7, 11);
            graph.AddEdge(7, 12);


            IIterator iterator = graph.GetIterator();

            foreach (var item in new List<string> { "A", "B", "C", "D" })
            {
                Observer plyer = new Observer(item);
                iterator.Attach(plyer);
            }

            iterator.Next();

            Console.ReadKey();
        }
    }
}
