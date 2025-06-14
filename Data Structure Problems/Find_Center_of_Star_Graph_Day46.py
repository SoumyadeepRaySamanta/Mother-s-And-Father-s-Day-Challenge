class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if len(edges) < 2:
            raise ValueError("Invalid input: at least two edges are required.")

        e1, e2 = edges[0], edges[1]

        for node in e1:
            if node in e2:
                return node

        raise ValueError("No common node found — not a valid star graph.")
