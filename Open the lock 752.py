from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Check if the initial combination is a dead end
        if "0000" in deadends:
            return -1
        
        # Initialize a queue with the starting combination '0000' and set of visited combinations
        queue = deque([('0000', 0)])
        visited = set(deadends)
        
        # Define a helper function to generate next possible combinations for a given combination
        def get_next_combinations(combination):
            next_combinations = []
            for i in range(4):
                # Generate combinations by incrementing and decrementing each digit
                next_digit = str((int(combination[i]) + 1) % 10)
                next_combinations.append(combination[:i] + next_digit + combination[i+1:])
                prev_digit = str((int(combination[i]) - 1 + 10) % 10)
                next_combinations.append(combination[:i] + prev_digit + combination[i+1:])
            return next_combinations
        
        # Perform BFS traversal
        while queue:
            current, turns = queue.popleft()
            # Check if the current combination is the target
            if current == target:
                return turns
            # Generate next possible combinations and add them to the queue if not visited
            for next_combination in get_next_combinations(current):
                if next_combination not in visited:
                    visited.add(next_combination)
                    queue.append((next_combination, turns + 1))
        
        # If target combination is not found, return -1
        return -1
