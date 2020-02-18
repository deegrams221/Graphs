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
        # Add verteces for parent and child
        # Add edge for parent, child

    # create empty list for new path

    # for each parent, child...
        # find path to starting node (using dfs)
        # check if new path is longer than previous...
            # if not, new path will replace old path

    # check if new path has no parents...
        # if yes, return -1
    # otherwise, return new path at 0 index
