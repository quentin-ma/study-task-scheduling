"""Module containing the priority functions that influence scheduling.

Each priority function takes a DAG and statically computes the
priority of each task (vertex).

As the simulator uses a min-heap to implement the priority queue,
negative values should be used when higher values represent higher
priorities.

Implemented functions: priority_by_{id, topological_order}
Functions with interfaces but no implementation:
    priority_by_{lpt, spt, successors, hlf, cp}
"""

def priority_by_id(graph):
    """Sets the priority of each task as its identifier.
    Smaller identifiers mean a higher priority.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities
    """
    for id, task in graph.vertices.items():
        task.priority = id
    

def priority_by_topological_order(graph):
    """Sets the priority of each task as its order in the topology.
    Smaller indexes mean a higher priority.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities
    """
    for i in range(len(graph.topological_order)):
        id = graph.topological_order[i]
        graph.vertices[id].priority = i

def priority_by_lpt(graph):
    """Sets the priority of each task as its load.
    Higher loads mean a higher priority.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities
    """
    for (load, task) in graph.vertices.items():
        task.priority *= int(task.load)
        

def priority_by_spt(graph):
    """Sets the priority of each task as its load.
    Lower loads mean a higher priority.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities
    """
    for (load, task) in graph.vertices.items():
        task.priority = int(task.load)

def priority_by_successors(graph):
    """Sets the priority of each task as its number of successors.
    Higher numbers of successors mean a higher priority.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities
    """
    for successors, task in graph.vertices.items():
        task.priority *= int(len(task.successors))

def priority_by_hlf(graph):
    """Sets the priority of each task following HLF.
    Higher levels mean higher priorities.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities

    Notes
    -----
    Highest Level First was proposed by Hu in 1961.
    Hu, T.C., 1961. Parallel sequencing and assembly line problems.
    Operations research, 9(6), pp.841-848.

    The algorithm is thought for unitary tasks and precedence trees.
    It is supposed to be adapted here to work with any kind of graph.
    """
    k = len(graph.vertices)
    for i in range(k):
        if graph.vertices[(k - i) - 1].id == 0:
            continue
        graph.vertices[i].priority = graph.vertices[(k - i) - 1].id * graph.vertices[i].priority

def dfs(graph, visited, v, id, i = 1, s = 1, hbl = 0):
    if i == 1 and len(graph.vertices[v].successors) == 0:
        return graph.vertices[v].load
    visited[v] = True
    assert(type(v) == int)
    if i == len(graph.vertices) - id - 1:
        return s
    else: 
        for u in graph.vertices[v].successors:
            if visited[u] == False:
                return dfs(graph, visited, u, id, i + 1, s + graph.vertices[v].load)

def priority_by_cp(graph):
    """Sets the priority of each task as its critical path value.
    Higher critical path values mean a higher priority.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities

    Notes
    -----
    Critical Path scheduling is described in Chapter 7.4.4 in
    Casanova, H., Legrand, A. and Robert, Y., 2008. Parallel algorithms. CRC Press.

    The critical path of a vertex here is to be computed based on
    the value of its bottom level. Chapter 7.3 in the same book explains how
    to compute the top and bottom levels of vertices.
    """
    size = len(graph.vertices)
    visited = [False] * size
    for i in range(len(graph.vertices)):
        s = dfs(graph, visited, i, graph.vertices[i].id) 
        graph.vertices[i].priority = -1 * s
        visited = [False] * size