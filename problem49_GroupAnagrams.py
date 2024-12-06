class Solution(object):
    def groupAnagrams(self, strs):
        """
        This function groups anagrams from the input list `strs`.
        An anagram is defined as a word formed by rearranging the letters of another word.
        """

        # Problem Explanation:
        # The goal is to group all strings that are anagrams of each other into sublists.
        # For example, in ["eat", "tea", "tan", "ate", "nat", "bat"]:
        # - "eat", "tea", and "ate" are anagrams and form one group.
        # - "tan" and "nat" are anagrams and form another group.
        # - "bat" has no anagram and forms its own group.
        # Return these groups in any order.

        # Dictionary to store groups of anagrams.
        # The key is a tuple of sorted characters (unique for each anagram group).
        # The value is a list of strings belonging to that anagram group.
        anagrams = {}

        # Iterate through each string in the input list.
        for s in strs:
            # Sort the characters in the string to create a unique key for anagrams.
            # Example: "eat", "tea", "ate" all become the tuple ('a', 'e', 't').
            key = tuple(sorted(s))

            # If the key is not in the dictionary, add it with an empty list.
            if key not in anagrams:
                anagrams[key] = []

            # Append the current string to the corresponding anagram group.
            anagrams[key].append(s)

        # Convert the dictionary values to a list, as the result should be a list of lists.
        return list(anagrams.values())

        # Time Complexity:
        # - Sorting each string takes O(K log K), where K is the average length of a string.
        # - Iterating through all strings in `strs` takes O(N), where N is the total number of strings.
        # - Therefore, the overall time complexity is O(N * K log K).

        # Space Complexity:
        # - The space complexity is O(N * K) to store all strings in the dictionary.
        # - Additional space is used for sorting each string, which is O(K).
        # - Therefore, the total space complexity is O(N * K).
