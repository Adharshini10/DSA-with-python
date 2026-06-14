# Day X: Two Sum Problem
# Goal: Find indices of two numbers that add up to a target.

# Approach 1: Brute Force (O(n^2))

def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # If no solution found


# Approach 2: Optimized (O(n))
# Using a dictionary (hash map) for faster lookup

def two_sum_optimized(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Example usage

numbers = [2, 7, 11, 15]
target = 9

print("Brute Force Result:", two_sum_bruteforce(numbers, target))   # Output: [0, 1]
print("Optimized Result:", two_sum_optimized(numbers, target))      # Output: [0, 1]

# How to run this file:
# Save it as ArraysTwoSum.py
# Open terminal/command prompt
# Navigate to the folder where the file is saved
# Run: python ArraysTwoSum.py
