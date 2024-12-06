class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Problem Explanation:
        ---------------------
        Implement a regex matching function with two special characters:
        - '.' matches any single character.
        - '*' matches zero or more of the preceding element.

        The function should determine whether the entire string `s` matches the pattern `p`.

        Dynamic Programming Approach:
        -----------------------------
        Use a 2D boolean DP table `dp` where:
        - dp[i][j] represents whether the first `i` characters of `s` match the first `j` characters of `p`.

        Key Observations:
        - If `p[j-1]` is a letter, it must match `s[i-1]`.
        - If `p[j-1]` is '.', it matches any character in `s`.
        - If `p[j-1]` is '*', it depends on whether the preceding character in `p` matches characters in `s`.

        Time Complexity: O(len(s) * len(p)) - We fill a DP table of size len(s) x len(p).
        Space Complexity: O(len(s) * len(p)) - The space required for the DP table.
        """
        
        # Step 1: Initialize a 2D DP table with False values
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Step 2: Empty string matches empty pattern
        dp[0][0] = True  # Base case: Both string and pattern are empty

        # Step 3: Handle patterns with '*' that can match zero preceding elements
        for j in range(1, len(p) + 1):  # O(len(p))
            if p[j - 1] == '*':  # '*' can match zero occurrences of the preceding element
                dp[0][j] = dp[0][j - 2]  # Check if the pattern without the last two characters matches

        # Step 4: Fill the DP table row by row
        for i in range(1, len(s) + 1):  # O(len(s))
            for j in range(1, len(p) + 1):  # O(len(p))
                # Case 1: Characters match directly or via '.' wildcard
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]  # Carry forward the match from the previous indices
                
                # Case 2: '*' can match zero or more of the preceding element
                elif p[j - 1] == '*':
                    # Option 1: '*' matches zero of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    
                    # Option 2: '*' matches one or more of the preceding element
                    # Check if the preceding element matches `s[i-1]` or is '.'
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        # Step 5: The final answer is stored in dp[len(s)][len(p)]
        return dp[len(s)][len(p)]

# Time Complexity: O(len(s) * len(p)) - Nested loops iterate over the lengths of `s` and `p`.
# Space Complexity: O(len(s) * len(p)) - DP table size is proportional to the product of the lengths.
