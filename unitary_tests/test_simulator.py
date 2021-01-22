#!/usr/bin/env python3

import unittest
import sys
# Add the parent directory to the path so we can import
# code from our simulator
sys.path.append('../')

from simulator.schedulers import priority_by_id
from simulator.graph import Graph
from simulator.simulator import simulate

class ByIDTest(unittest.TestCase):
    def test_simple(self):
        graph = Graph.generate_graph(20, (1, 5), (1, 3), True, 100)
        priority_by_id(graph)
        makespan = simulate(graph, 10, False)
        self.assertEqual(makespan, 22)
        graph.reset_predecessors()
        makespan = simulate(graph, 2, False)
        self.assertEqual(makespan, 30)


if __name__ == '__main__':
    unittest.main()
