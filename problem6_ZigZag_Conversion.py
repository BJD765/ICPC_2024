class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Problem Explanation:
        ---------------------
        The goal is to rearrange the string `s` into a zigzag pattern with `numRows` rows
        and then read the characters row by row to generate the result.
        
        Zigzag Pattern Example for s = "PAYPALISHIRING", numRows = 4:
        P     I     N
        A   L S   I G
        Y A   H R
        P     I

        The result after reading row by row is: "PINALSIGYAHRPI"

        Key Observations:
        -----------------
        1. Characters move row-by-row in a "zigzag" fashion:
           - Downward until the bottom row is reached.
           - Upward diagonally until the top row is reached, and so on.
        2. Special cases:
           - If `numRows` is 1 or greater than or equal to the length of `s`, the string remains unchanged.

        Time Complexity: O(n), where n is the length of the string `s`.
        Space Complexity: O(n), for storing rows of characters.
        """
        
        # Handle special cases where zigzag conversion is unnecessary
        if numRows == 1 or numRows >= len(s):  # O(1)
            return s

        # Step 1: Create an array to store characters for each row
        rows = [''] * numRows  # O(numRows)

        # Step 2: Initialize variables to track the current row and direction
        current_row = 0  # Start at the first row
        going_down = False  # Indicates the direction (downward or upward)

        # Step 3: Traverse the string character by character
        for char in s:  # O(n)
            # Append the current character to the corresponding row
            rows[current_row] += char  # O(1)

            # Step 4: Change direction if the top or bottom row is reached
            if current_row == 0:  # Top row, start moving downward
                going_down = True
            elif current_row == numRows - 1:  # Bottom row, start moving upward
                going_down = False

            # Step 5: Update the current row based on direction
            current_row += 1 if going_down else -1  # O(1)

        # Step 6: Combine all rows to form the final zigzag-converted string
        return ''.join(rows)  # O(n)

# Time Complexity: O(n)
# Explanation: We iterate through the string once (O(n)), appending characters to rows (O(1)).
# Joining the rows into the final string is also O(n).
# Space Complexity: O(n)
# Explanation: We use an array `rows` of size `numRows`, where each row can store up to all the characters in `s`.
