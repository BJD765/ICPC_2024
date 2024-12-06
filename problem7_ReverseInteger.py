class Solution:
    def reverse(self, x: int) -> int:
        """
        Problem Explanation:
        ---------------------
        Given a signed 32-bit integer `x`, we need to reverse its digits while preserving the sign.
        The output must:
          1. Be within the range of a 32-bit signed integer: [-2^31, 2^31 - 1].
          2. Return 0 if reversing `x` causes overflow (i.e., exceeds this range).
        Assumption: We cannot store 64-bit integers, so operations must remain within 32-bit bounds.

        Example:
        --------
        Input: x = 123
        Output: 321

        Input: x = -123
        Output: -321

        Input: x = 120
        Output: 21
        """

        # Step 1: Define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # O(1)

        # Step 2: Determine the sign of `x`
        # If `x` is negative, set `sign` to -1; otherwise, set it to 1
        sign = -1 if x < 0 else 1  # O(1)

        # Step 3: Work with the absolute value of `x` to simplify digit reversal
        x_abs = abs(x)  # O(1)

        # Step 4: Initialize the reversed number as 0
        reversed_x = 0  # O(1)

        # Step 5: Reverse the digits of `x_abs` by iterating through its digits
        while x_abs > 0:  # Loop runs O(log10(x)) times, where x is the input value
            # Extract the last digit of `x_abs`
            digit = x_abs % 10  # O(1)

            # Append the digit to the reversed number
            # Multiply `reversed_x` by 10 (to shift left) and add the current digit
            reversed_x = reversed_x * 10 + digit  # O(1)

            # Remove the last digit from `x_abs`
            x_abs //= 10  # O(1)

        # Step 6: Restore the sign of the reversed number
        reversed_x *= sign  # O(1)

        # Step 7: Check for overflow
        # If `reversed_x` exceeds the range of a 32-bit signed integer, return 0
        if reversed_x < INT_MIN or reversed_x > INT_MAX:  # O(1)
            return 0  # O(1)

        # Step 8: Return the reversed number if no overflow occurred
        return reversed_x  # O(1)

# Time Complexity: O(log10(x))
# - The while loop iterates once for each digit in the input `x`, which is proportional to log10(x).
# Space Complexity: O(1)
# - The algorithm uses a constant amount of memory regardless of the size of the input.
