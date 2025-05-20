class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize minOpen and maxOpen to 0
        # minOpen: minimum number of open parentheses at this point
        # maxOpen: maximum number of open parentheses at this point
        minOpen = maxOpen = 0

        for char in s:
            if char == '(':
                minOpen += 1
                maxOpen += 1
            elif char == ')':
                minOpen -= 1
                maxOpen -= 1
            else:  # char == '*'
                minOpen -= 1     # Treat '*' as ')'
                maxOpen += 1     # Or treat '*' as '('

            # If maxOpen < 0, there are too many ')'
            if maxOpen < 0:
                return False

            # minOpen should not be negative
            minOpen = max(minOpen, 0)

        # If minOpen is 0, a valid configuration is possible
        return minOpen == 0
