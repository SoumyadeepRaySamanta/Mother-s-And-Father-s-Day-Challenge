class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.isqrt(c))  # integer square root of c
        
        while a <= b:
            current = a * a + b * b
            if current == c:
                return True
            elif current < c:
                a += 1
            else:
                b -= 1
        
        return False
