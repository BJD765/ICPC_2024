#include <stdio.h>

#define MOD 1000000007 // Define the modulus to prevent overflow
/*
 * Problem Explanation:
 * Given an array `nums`, the task is to find the number of non-empty subsets of `nums`
 * where the product of the subset's elements is a square-free integer.
 *
 * A square-free integer is an integer that is not divisible by any square number
 * other than 1 (e.g., 6 is square-free, but 12 is not since it is divisible by 4).
 *
 * Subsets are defined as any selection of elements from `nums` (not necessarily contiguous).
 * The solution must exclude the empty subset and return the result modulo 10^9 + 7.
 */


/*
 * Function to calculate the number of square-free subsets.
 * @param nums - input array of positive integers.
 * @param numsSize - size of the array.
 * @return number of square-free subsets modulo MOD.
 */
int squareFreeSubsets(int* nums, int numsSize) {
    // `dp[i][j]` stores the number of valid subsets starting from index `i`
    // with bitmask `j` representing the primes included in the subset product.
    long long dp[numsSize + 1][1024];

    // First 10 prime numbers, covering all possible prime factors for numbers <= 30.
    int primes[10] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

    // Base case: For subsets beyond the last index, there is 1 valid subset (the empty subset).
    for (int i = 0; i < 1024; i++) {
        dp[numsSize][i] = 1;
    }

    // Process the array in reverse to build the DP table
    for (int i = numsSize - 1; i >= 0; i--) {
        for (int j = 1023; j >= 0; j--) {
            // Start with subsets that do not include the current element
            dp[i][j] = dp[i + 1][j];

            int ck = 1; // Flag to check if current element can be included
            int nj = j; // Bitmask for the current subset
            int ele = nums[i]; // Current element

            // Factorize the element and update the bitmask
            for (int k = 0; k < 10; k++) {
                // Check if the current prime divides `ele`
                while (ele % primes[k] == 0) {
                    ele /= primes[k]; // Remove the prime factor
                    // If the prime is already in the subset, mark it invalid
                    if ((nj & (1 << k)) >> k) {
                        ck = 0; // Conflict with existing prime factor
                        break;
                    } else {
                        nj |= (1 << k); // Add the prime to the bitmask
                    }
                }
                if (!ck) break; // Stop if invalid
            }

            // If the current element can be included, update the DP table
            if (ck) {
                dp[i][j] = (dp[i][j] + dp[i + 1][nj]) % MOD;
            }
        }
    }

    // Subtract 1 to exclude the empty subset and return the result
    return (dp[0][0] - 1 + MOD) % MOD;
}

/*
 * Time Complexity:
 * - The outer loop iterates over all elements in the array `nums`, which is `O(n)`.
 * - The inner loop iterates over all possible bitmasks (1024 states), which is `O(2^10)`.
 * - Inside the inner loop, we factorize the current element into primes, which takes `O(10)` (fixed, as we only have 10 primes).
 * - Overall: O(n × 1024 × 10) = O(n × 10240) = O(n), where `n` is the size of the input array.
 *
 * Space Complexity:
 * - The DP table `dp[i][j]` requires `O(n × 1024)` space.
 * - Other variables (like `primes` and auxiliary variables) use `O(1)` space.
 * - Overall: O(n × 1024) space.
 */
