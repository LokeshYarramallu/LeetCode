from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Base case: if there's only one node, return it
        if n == 1:
            return [0]
        
        # Create an adjacency list to represent the graph
        adjacency_list = defaultdict(list)
        
        # Initialize a list to store the degree of each node
        degree = [0] * n
        
        # Populate the adjacency list and update the degree of each node
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Initialize a deque with the leaves (nodes with degree 1)
        leaves = deque([i for i in range(n) if degree[i] == 1])
        
        # Variable to keep track of the remaining nodes
        remaining_nodes = n
        
        # Continue until there are only 1 or 2 nodes left
        while remaining_nodes > 2:
            # Count the number of leaves in this iteration
            leaves_count = len(leaves)
            # Update the count of remaining nodes
            remaining_nodes -= leaves_count
            
            # Process each leaf
            for _ in range(leaves_count):
                # Remove a leaf from the deque
                leaf = leaves.popleft()
                # Decrease the degree of its neighbors
                for neighbor in adjacency_list[leaf]:
                    degree[neighbor] -= 1
                    # If the degree becomes 1, it becomes a new leaf
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        # Convert the deque of leaves to a list and return
        return list(leaves)
