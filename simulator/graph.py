"""Module containing the generation of tasks for scheduling algorithms.

Each task contains parameters that indicate its identifier, its processing time,
dependencies, and others.
"""


import random

class Task:
    """
    Task object.

    Attributes
    ----------
    id : int
        Task identifier
    load : int
        Processing time of the task (also known as its weight)
    predecessors : set of Task.id
        Predecessors of the task
    successors : set of Task.id
        Successors of the task
    priority : int
        Priority of the task - to be computed
    top_level : int
        Top level of the task (largest weight of a path from a top vertex,
        excluding the tasks' weight) - to be computed
    bottom_level : int
        Bottom level of the task (largest weight of a path from a bottom
        vertex, including the tasks' weight) - to be computed
    """
    def __init__(self, id, load):
        self.id = id
        self.load = load
        self.predecessors = set()
        self.successors = set()
        self.priority = -1
        self.top_level = -1
        self.bottom_level = -1

    """Simplified representation of a task"""
    def __repr__(self):
        #return f'task {self.id}'  # simplified version
        return (f'Task {self.id} (load={self.load}, pred={self.predecessors}'+
                f', succ={self.successors}, priority={self.priority})')

    """Less than operator using the priority of the tasks"""
    def __lt__(self, other):
        return self.priority < other.priority


class Graph:
    """
    DAG of tasks for scheduling algorithms.

    Attributes
    ----------
    vertices : dict of (Task.id, Task)
        Tasks in the graph
    topological_order : list of Task.id
        List of tasks in topological order
    """
    def __init__(self):
        self.vertices = dict()
        self.topological_order = list()

    def __repr__(self):
        """Simplified representation of the graph"""
        text = 'Vertices:\n'
        for vertex in self.vertices.values():
            text += str(vertex) + '\n'
        text += 'Topological order:\n'
        text += str(self.topological_order)
        return text

    def topological_ordering(self):
        """Computed a topological order for the graph"""
        self.topological_order = list()
        checked_vertices = set()  # covered vertices
        to_check = set()          # successors of covered vertices
        # First step: find all top (entry) vertices
        for id, vertex in self.vertices.items():
            # No predecessor == top
            if not vertex.predecessors:
                checked_vertices.add(id)
                self.topological_order.append(id)
                # Adds successors to the list of vertices to check
                to_check.update(list(vertex.successors))
        # Second step: find an order for all other vertices
        while to_check:
            # Making sure the traversal is not adding a vertex more than once
            to_check = to_check - checked_vertices
            to_check_later = set()  # Vertices to check in another iteration
            # Iterates over vertices to check
            for id in to_check:
                # Checks if all predecessors have been checked
                vertex = self.vertices[id]
                if vertex.predecessors.issubset(checked_vertices):
                    # Then it can join the topological order
                    self.topological_order.append(id)
                    # Adds its successors can be considered for checking
                    to_check_later.update(list(vertex.successors))
                    # And adds it to the list of checked vertices
                    checked_vertices.add(id)
                else:
                    # Adds it to be checked again later
                    to_check_later.add(id)
            # Updates the set to check for a new pass
            to_check = to_check_later
        # Checking if all vertices are in the topological_order
        if len(self.vertices) != len(self.topological_order):
            print('Error: topological order is missing items.')

    def reset_predecessors(self):
        """Resets the lists of predecessors of each task"""
        for id, task in self.vertices.items():
            for succ_id in task.successors:
                self.vertices[succ_id].predecessors.add(id)

    @staticmethod
    def generate_graph(
            num_tasks,
            load_range,
            dependency_range,
            rename=False,
            rng_seed=None
            ):
        """
        Generates a graph of tasks.

        Parameters
        ----------
        num_tasks : int
            Number of tasks in the graph
        load_range : (int, int)
            Minimum and maximum loads for tasks
        dependency_range : (int, int)
            Minimum and maximum number of predecessors for each task
        rename = bool [default = False]
            True if task identifiers have to be shuffled
        rng_seed : int [optional]
            Random number generator seed

        Returns
        -------
        Graph object
            DAG of tasks
        """
        graph = Graph()        # graph to generate and return
        min_load, max_load = load_range
        min_dep, max_dep = dependency_range

        # Translation of ordered to unordered ids if necessary
        id = [i for i in range(num_tasks)]
        if rename == True:
            random.seed(rng_seed-1)  # set random seed for the shuffle
            random.shuffle(id)

        random.seed(rng_seed)  # set random seed
        # Generate tasks
        # The first one has to be a top (entry) vertex
        load = random.randrange(min_load, max_load)
        graph.vertices[id[0]] = Task(id[0], load)
        # The other ones need to have their dependencies created
        for task in range(1, num_tasks):
            # Creates task
            load = random.randrange(min_load, max_load)
            graph.vertices[id[task]] = Task(id[task], load)
            # Checks how many dependencies it should have
            num_dep = random.randrange(min_dep, max_dep)
            # Checks if we have enough tasks to cover that
            if num_dep < task:  # we do
                # Gets a sample of valid predecessors and updates them
                for pred in random.sample(range(task), k=num_dep):
                    graph.vertices[id[task]].predecessors.add(id[pred])
                    graph.vertices[id[pred]].successors.add(id[task])
            else:  # we do not have enough tasks in the graph to depend
                # so we just use all the previous tasks
                for pred in range(task):
                    graph.vertices[id[task]].predecessors.add(id[pred])
                    graph.vertices[id[pred]].successors.add(id[task])

        # Last thing to generate: the topological order
        graph.topological_ordering()

        return graph

