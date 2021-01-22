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
    #TODO

def priority_by_spt(graph):
    """Sets the priority of each task as its load.
    Lower loads mean a higher priority.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities
    """
    #TODO

def priority_by_successors(graph):
    """Sets the priority of each task as its number of successors.
    Higher numbers of successors mean a higher priority.

    Parameters
    ----------
    graph : Graph object
        Graph to update priorities
    """
    #TODO

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
    # TODO

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
    #TODO
