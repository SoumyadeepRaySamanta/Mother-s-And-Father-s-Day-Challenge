class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            # Step 1: Flip the row by reversing it
            row.reverse()
            
            # Step 2: Invert the row by replacing 0 -> 1 and 1 -> 0
            for i in range(len(row)):
                row[i] ^= 1  # XOR with 1 flips the bit (0->1, 1->0)

        return image
