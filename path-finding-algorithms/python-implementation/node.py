from __future__ import annotations # This allows us to forward reference - only in 3.10
from typing import Dict, List


class Node:
    """
    This class represents a node on a weighted graph. 
    Each node has its initial cost and edges with their weightings pointing to other nodes.
    """
    
    def __init__(self, initial_cost: int, edges: Dict[Node, int], is_source: bool = False, is_target: bool = False) -> None:
        self.node_cost = initial_cost
        self.edges = edges
        self.is_source = is_source
        self.is_target = is_target

    def update_node_cost(self, new_cost: int) -> None:
        self.node_cost = new_cost


def create_create_node(node_cost: int, edges: Dict[Node, int], is_source: bool = False, is_target: bool = False) -> Node:
    return Node(node_cost, edges, is_source, is_target)

