'''
Given an integer array nums, return true
if any value appears at least twice in the
array, and return false if every number
is distinct.

Example 1:
    Input: nums = [1, 2, 3, 1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

nums = [1]
output: False

nums = [0, 0, 0, 0]
output: True

Brainstorm:
        Sort Array
            Time: O(nlogn)
            Space: O(1)
        Compare Hashset length with OG array lenth
            Time: O(n)
            Space: O(n)
        Brute Force Way:
            Time: O(n^2)
            Space: O(1)



'''

def contains_duplicate(nums):
    duplicate = set()
    for num in nums:
        if num in duplicate: return True
        duplicate.add(num)
    return False






print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
