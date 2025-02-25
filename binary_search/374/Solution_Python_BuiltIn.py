# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import bisect

class Solution:
    def guessNumber(self, n: int) -> int:
        # Use binary search to find the guessed number.
        # Define the bisect function to compare guess results.
        def guess_compare(x):
            # Return the result of the guess API call:
            # Negative result if our guess is higher (-1),
            # Positive if our guess is lower (1),
            # Zero if our guess is correct (0)
            return -guess(x)

        # Use the bisect function to find the correct number.
        # We make use of the `key` parameter to provide our custom comparison
        # function which uses the guess API as the comparison logic.
        return bisect.bisect_left(range(1, n + 1), 0, key=guess_compare) + 1

# Note: The original implementation used bisect.bisect, which by default assumes
# an insertion point that would maintain order. In this case, we want the exact position
# where the guess result is 0, hence bisect_left is more appropriate.
