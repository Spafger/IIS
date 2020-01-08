using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DepthFirstSearch
{
    class GraphNumerator : IIterator
    {
        Dictionary<int, HashSet<int>> Graph { get; set; }
        private List<IObserver> observers = new List<IObserver>();


        private int vertex;
        private HashSet<int> visited = new HashSet<int>();
        private Stack<int> stack = new Stack<int>();

        public GraphNumerator(Dictionary<int, HashSet<int>> graph)
        {
            vertex = 1;
            Graph = graph;
            stack.Push(vertex);
        }


        public void Next()
        {
            Traverse(vertex, visited);
        }

        private void Traverse(int v, HashSet<int> visited)
        {
           
            visited.Add(v);
            Notify(v);
            if (Graph.ContainsKey(v))
            {
           
                foreach (int neighbour in Graph[v].Where(a => !visited.Contains(a)))
                {
                    Traverse(neighbour, visited);
                }
            }
        }

        public void Attach(IObserver observer)
        {
            observers.Add(observer);
        }

        private void Notify(int i)
        {
            foreach (var observer in observers)
            {
                observer.Update(observer, i);
            }
        }
    }
}
