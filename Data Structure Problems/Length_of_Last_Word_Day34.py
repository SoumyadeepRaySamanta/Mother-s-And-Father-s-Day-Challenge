"""
        This function returns the length of the last word in a given string.
        A word is defined as a maximal sequence of non-space characters.
        """

        # Step 1: Strip any trailing spaces (if the string ends with spaces, the last word is before them)
        s = s.rstrip()

        # Step 2: Initialize a counter for the last word's length
        length = 0

        # Step 3: Iterate the string in reverse (from the end to the beginning)
        for char in reversed(s):
            if char == ' ':
                # As soon as we hit a space after starting to count, we break
                break
            length += 1  # Increment length for each character in the last word

        return length
