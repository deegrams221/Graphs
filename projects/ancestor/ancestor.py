"""
Given the dataset and the ID of an individual in the dataset returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.

- list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
"""
# import graph and util
from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # build graph
    g = Graph()
    # for parents and children in ancestors...
    for (parent, child) in ancestors:
        # Add verteces for parent and child
        g.add_vertex(parent)
        g.add_vertex(child)
        # Add edge for parent, child
        g.add_edge(parent, child)

    # create empty list for new path
    new_path = []

    # for each parent, child...
    for (parent, child) in ancestors:
        # find path to starting node (using dfs)
        path = g.dfs(parent, starting_node)
        # check if new path is longer than previous...
        if path is not None and len(path) > len(new_path):
            # if not, new path will replace old path
            new_path = path.copy()

    # check if new path has no parents...
    if len(new_path) <= 1:
        # if yes, return -1
        return -1
    # otherwise, return new path at 0 index
    return new_path[0]

