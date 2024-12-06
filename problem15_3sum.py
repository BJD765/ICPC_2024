class Solution(object):
    def threeSum(self, nums):
        """
        This function finds all unique triplets in the array `nums` such that their sum is zero.
        """

        # Problem explanation:
        # The goal is to find all unique triplets [nums[i], nums[j], nums[k]] in the array
        # such that:
        # 1. nums[i] + nums[j] + nums[k] == 0
        # 2. i, j, and k are distinct indices.
        # 3. The solution set must not contain duplicate triplets.
        #
        # Approach:
        # - Use sorting to simplify duplicate handling and efficient two-pointer traversal.
        # - For each number in the array, consider it as the first number in a triplet.
        # - Use two pointers to find the remaining two numbers that sum to the target (-nums[i]).
        # - Skip duplicates to ensure unique triplets in the result.

        # Sort the array to enable two-pointer traversal and simplify duplicate handling.
        nums.sort()

        # Initialize the result list to store the unique triplets.
        result = []

        # Iterate over the array, treating each number as the first number in a potential triplet.
        for i in range(len(nums) - 2):

            # If the current number is the same as the previous one, skip it to avoid duplicates.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers: `left` starts after `i`, and `right` starts at the end of the array.
            left, right = i + 1, len(nums) - 1

            # While the two pointers do not overlap:
            while left < right:
                # Calculate the sum of the triplet.
                total = nums[i] + nums[left] + nums[right]

                # If the sum is less than zero, move the left pointer to the right to increase the sum.
                if total < 0:
                    left += 1

                # If the sum is greater than zero, move the right pointer to the left to decrease the sum.
                elif total > 0:
                    right -= 1

                # If the sum is exactly zero, we found a valid triplet.
                else:
                    # Add the triplet to the result list.
                    result.append([nums[i], nums[left], nums[right]])

                    # Move the left pointer to skip duplicates of `nums[left]`.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Move the right pointer to skip duplicates of `nums[right]`.
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers to continue searching for other triplets.
                    left += 1
                    right -= 1

        # Return the list of unique triplets.
        return result
