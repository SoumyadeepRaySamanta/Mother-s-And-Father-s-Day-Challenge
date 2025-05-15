class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        count = 9
        start = 1

        # Find the length of the number that contains the nth digit
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Find the actual number where the nth digit is from
        num = start + (n - 1) // length
        # Find the digit index in that number
        digit_index = (n - 1) % length
        return int(str(num)[digit_index])
