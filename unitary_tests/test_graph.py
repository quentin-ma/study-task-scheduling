#!/usr/bin/env python3

import unittest
import sys
# Add the parent directory to the path so we can import
# code from our simulator
sys.path.append('../')

from simulator.graph import Graph, Task


class TaskTest(unittest.TestCase):
    def test_init(self):
        task = Task(10, 100)
        self.assertEqual(task.id, 10)
        self.assertEqual(task.load, 100)
        self.assertFalse(task.predecessors)
        self.assertFalse(task.successors)
        self.assertEqual(task.priority, -1)
        self.assertEqual(task.top_level, -1)
        self.assertEqual(task.bottom_level, -1)

    def test_comparison(self):
        task1 = Task(1000, 10)
        task1.priority = 100
        task2 = Task(2000, 5)
        task2.priority = 50
        self.assertTrue(task2 < task1)
        self.assertFalse(task1 < task2)


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph1 = Graph.generate_graph(6, (1, 10), (0, 3), False, 5)
        self.graph2 = Graph.generate_graph(6, (1, 10), (0, 3), True, 5)

    def test_attributes(self):
        vertices = self.graph1.vertices
        self.assertEqual(vertices[0].load, 5)
        self.assertEqual(vertices[1].load, 6)
        self.assertEqual(vertices[2].load, 9)
        self.assertEqual(vertices[3].load, 8)
        self.assertEqual(vertices[4].load, 1)
        self.assertEqual(vertices[5].load, 2)

        self.assertTrue(1 in vertices[0].successors)
        self.assertTrue(2 not in vertices[0].successors)
        self.assertTrue(3 not in vertices[0].successors)
        self.assertTrue(4 not in vertices[0].successors)
        self.assertTrue(5 not in vertices[0].successors)
        self.assertTrue(5 in vertices[3].successors)

        self.assertTrue(0 in vertices[1].predecessors)
        self.assertTrue(3 in vertices[5].predecessors)
        self.assertTrue(2 not in vertices[1].predecessors)
        self.assertTrue(3 not in vertices[1].predecessors)
        self.assertTrue(4 not in vertices[1].predecessors)
        self.assertTrue(5 not in vertices[1].predecessors)

        vertices = self.graph2.vertices
        self.assertEqual(vertices[3].load, 5)
        self.assertEqual(vertices[5].load, 6)
        self.assertEqual(vertices[4].load, 9)
        self.assertEqual(vertices[0].load, 8)
        self.assertEqual(vertices[2].load, 1)
        self.assertEqual(vertices[1].load, 2)

    def test_topological_order(self):
        topo1 = self.graph1.topological_order
        topo2 = self.graph2.topological_order

        self.assertEqual(topo1[0], 0)
        self.assertEqual(topo1[1], 2)
        self.assertEqual(topo1[2], 3)
        self.assertEqual(topo1[3], 4)
        self.assertEqual(topo1[4], 1)
        self.assertEqual(topo1[5], 5)

        self.assertEqual(topo2[0], 3)
        self.assertEqual(topo2[1], 4)
        self.assertEqual(topo2[2], 0)
        self.assertEqual(topo2[3], 2)
        self.assertEqual(topo2[4], 1)
        self.assertEqual(topo2[5], 5)


if __name__ == '__main__':
    unittest.main()
