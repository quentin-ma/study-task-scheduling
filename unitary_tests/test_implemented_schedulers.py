#!/usr/bin/env python3

import unittest
import sys
# Add the parent directory to the path so we can import
# code from our simulator
sys.path.append('../')

from simulator.schedulers import priority_by_id, priority_by_topological_order
from simulator.graph import Graph


class ByIDTest(unittest.TestCase):
    def test_simple(self):
        graph = Graph.generate_graph(6, (1, 10), (0, 3), False, 10)
        priority_by_id(graph)
        self.assertEqual(graph.vertices[0].priority, 0)
        self.assertEqual(graph.vertices[1].priority, 1)
        self.assertEqual(graph.vertices[2].priority, 2)
        self.assertEqual(graph.vertices[3].priority, 3)
        self.assertEqual(graph.vertices[4].priority, 4)
        self.assertEqual(graph.vertices[5].priority, 5)


class ByTopoTest(unittest.TestCase):
    def test_simple(self):
        graph = Graph.generate_graph(6, (1, 10), (0, 3), False, 10)
        priority_by_topological_order(graph)
        self.assertEqual(graph.vertices[0].priority, 0)
        self.assertEqual(graph.vertices[1].priority, 3)
        self.assertEqual(graph.vertices[2].priority, 1)
        self.assertEqual(graph.vertices[3].priority, 5)
        self.assertEqual(graph.vertices[4].priority, 2)
        self.assertEqual(graph.vertices[5].priority, 4)


if __name__ == '__main__':
    unittest.main()
