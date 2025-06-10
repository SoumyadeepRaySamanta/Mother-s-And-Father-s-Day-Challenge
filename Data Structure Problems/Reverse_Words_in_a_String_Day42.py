class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Strip leading and trailing spaces
        # and split the string into words.
        # The split() function (without arguments) automatically
        # handles multiple spaces between words.
        words = s.strip().split()
        
        # Step 2: Reverse the list of words in-place.
        # This places the last word first and so on.
        words.reverse()
        
        # Step 3: Join the reversed list of words into a single string.
        # Words are joined with a single space between them.
        return ' '.join(words)
