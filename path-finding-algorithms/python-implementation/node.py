from __future__ import annotations # This allows us to forward reference - only in 3.10
from typing import Dict, List, Optional
from random import randint
import json


class Node:
    """
    This class represents a node on a weighted graph. 
    Each node has its initial cost and edges with their weightings pointing to other nodes.
    """
    
    def __init__(self, id: int, initial_cost: int, edges: Optional[Dict[Node, int]] = None, is_source: bool = False, is_target: bool = False) -> None:
        self.id = id
        self.node_cost = initial_cost
        self.edges = edges if edges is not None else {}
        self.is_source = is_source
        self.is_target = is_target

    def update_node_cost(self, new_cost: int) -> None:
        self.node_cost = new_cost


def generate_connected_graph(num_nodes: int) -> List[Node]:
    nodes = [Node(id=i, initial_cost=randint(1,100)) for i in range(num_nodes)]
    
    # Connect everything first linearly
    for i in range(num_nodes - 1):
        weight = randint(1, 20)
        nodes[i].edges[nodes[i+1]] = weight

    # Add connections if needed
    for i in range(num_nodes):
        current_node = nodes[i]
        for _ in range(randint(0, 2)):
            target_index = randint(0, num_nodes - 1)
            target_node = nodes[target_index]
            if target_index != i and target_node not in current_node.edges:
                weight = randint(1, 20)
                current_node.edges[target_node] = weight
    
    return nodes


def represent_graph_as_text(nodes: List[Node]) -> Dict[int, dict]:
    representation = {}
    for node in nodes:
        connected_ids = [neighbor.id for neighbor in node.edges.keys()]
        representation[node.id] = {
            "node_cost": node.node_cost,
            "connections": connected_ids
        }
    return representation


if __name__=="__main__":
    graph_nodes = generate_connected_graph(num_nodes=6)
    print(json.dumps(represent_graph_as_text(nodes=graph_nodes), indent=2))