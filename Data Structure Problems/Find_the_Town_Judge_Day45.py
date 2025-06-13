class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Algorithm:
        - Create a trust score array of size n + 1 (1-indexed).
        - For each trust[a, b]:
            - Decrease a's score (a trusts someone)
            - Increase b's score (b is trusted by someone)
        - The judge will have score == n - 1 (trusted by everyone else, trusts no one)

        Time Complexity: O(n + t), where t = len(trust)
        Space Complexity: O(n)
        """

        trust_score = [0] * (n + 1)

        for a, b in trust:
            trust_score[a] -= 1  # a trusts someone → not judge
            trust_score[b] += 1  # b is trusted → could be judge

        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i

        return -1
