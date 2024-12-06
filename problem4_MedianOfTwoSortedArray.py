class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Find the median of two sorted arrays using binary search.

        Time Complexity:
        ----------------
        O(log(min(m, n))) where m and n are the sizes of nums1 and nums2.

        Space Complexity:
        -----------------
        O(1), as no additional data structures are used.

        Parameters:
        -----------
        nums1: List[int] - First sorted array.
        nums2: List[int] - Second sorted array.

        Returns:
        --------
        float - The median of the two sorted arrays.
        """

        # Ensure nums1 is the smaller array for binary search efficiency
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # Binary search bounds
        left, right = 0, m

        while left <= right:
            # Partition the arrays
            partition1 = (left + right) // 2  # Mid-point of nums1
            partition2 = (m + n + 1) // 2 - partition1  # Complement in nums2
            
            # Left and right elements around the partition
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if the partition is valid
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Correct partition found
                if (m + n) % 2 == 0:
                    # Even length case: median is the average of two middle elements
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    # Odd length case: median is the max of the left elements
                    return max(maxLeft1, maxLeft2)

            elif maxLeft1 > minRight2:
                # Move the partition1 to the left
                right = partition1 - 1
            else:
                # Move the partition1 to the right
                left = partition1 + 1
