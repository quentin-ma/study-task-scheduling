#!/usr/bin/env python3

import unittest
import sys
# Add the parent directory to the path so we can import
# code from our simulator
sys.path.append('../')

from simulator.schedulers import priority_by_lpt, priority_by_spt, priority_by_successors, priority_by_hlf, priority_by_cp
from simulator.graph import Graph


class ByLPTTest(unittest.TestCase):
    def test_simple(self):
        graph = Graph.generate_graph(6, (1, 10), (0, 3), False, 10)
        priority_by_lpt(graph)
        self.assertEqual(graph.vertices[0].priority, -1)
        self.assertEqual(graph.vertices[1].priority, -7)
        self.assertEqual(graph.vertices[2].priority, -1)
        self.assertEqual(graph.vertices[3].priority, -8)
        self.assertEqual(graph.vertices[4].priority, -3)
        self.assertEqual(graph.vertices[5].priority, -9)


class BySPTTest(unittest.TestCase):
    def test_simple(self):
        graph = Graph.generate_graph(6, (1, 10), (0, 3), False, 10)
        priority_by_spt(graph)
        self.assertEqual(graph.vertices[0].priority, 1)
        self.assertEqual(graph.vertices[1].priority, 7)
        self.assertEqual(graph.vertices[2].priority, 1)
        self.assertEqual(graph.vertices[3].priority, 8)
        self.assertEqual(graph.vertices[4].priority, 3)
        self.assertEqual(graph.vertices[5].priority, 9)


class BySUCCTest(unittest.TestCase):
    def test_simple(self):
        graph = Graph.generate_graph(6, (1, 10), (0, 4), False, 10)
        priority_by_successors(graph)
        self.assertEqual(graph.vertices[0].priority, -3)
        self.assertEqual(graph.vertices[1].priority, -1)
        self.assertEqual(graph.vertices[2].priority, -2)
        self.assertEqual(graph.vertices[3].priority, -1)
        self.assertEqual(graph.vertices[4].priority, 0)
        self.assertEqual(graph.vertices[5].priority, 0)


class ByHLFTest(unittest.TestCase):
    def test_simple(self):
        graph = Graph.generate_graph(6, (1, 10), (0, 4), False, 10)
        priority_by_hlf(graph)
        self.assertEqual(graph.vertices[0].priority, -5)
        self.assertEqual(graph.vertices[1].priority, -4)
        self.assertEqual(graph.vertices[2].priority, -3)
        self.assertEqual(graph.vertices[3].priority, -2)
        self.assertEqual(graph.vertices[4].priority, -1)
        self.assertEqual(graph.vertices[5].priority, -1)


class ByCPTest(unittest.TestCase):
    def test_simple(self):
        graph = Graph.generate_graph(6, (1, 10), (0, 4), False, 10)
        priority_by_cp(graph)
        self.assertEqual(graph.vertices[0].priority, -18)
        self.assertEqual(graph.vertices[1].priority, -17)
        self.assertEqual(graph.vertices[2].priority, -10)
        self.assertEqual(graph.vertices[3].priority, -9)
        self.assertEqual(graph.vertices[4].priority, -1)
        self.assertEqual(graph.vertices[5].priority, -6)


if __name__ == '__main__':
    unittest.main()
