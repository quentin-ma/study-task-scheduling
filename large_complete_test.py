"""Example of use of the simulator.

To run, use 'python3 large_complete_test.py'.

"""

import simulator.schedulers as schedulers
from simulator.graph import Graph
from simulator.simulator import simulate

print('Testing 10000 tasks over 20 resources for all priorities')
graph = Graph.generate_graph(10000, (2, 20), (1, 20), True, 1234)

print('Priority by identifier')
schedulers.priority_by_id(graph)
simulate(graph, 20, False)
graph.reset_predecessors()

print('Priority by topological order')
schedulers.priority_by_topological_order(graph)
simulate(graph, 20, False)
graph.reset_predecessors()

print('Priority by largest processing time')
schedulers.priority_by_lpt(graph)
simulate(graph, 20, False)
graph.reset_predecessors()

print('Priority by smallest processing time')
schedulers.priority_by_spt(graph)
simulate(graph, 20, False)
graph.reset_predecessors()

print('Priority by number of successors')
schedulers.priority_by_successors(graph)
simulate(graph, 20, False)
graph.reset_predecessors()

print('Priority by Highest Level First (HLF)')
schedulers.priority_by_hlf(graph)
simulate(graph, 20, False)
graph.reset_predecessors()

print('Priority by Critical Path (CP)')
schedulers.priority_by_cp(graph)
simulate(graph, 20, False)
