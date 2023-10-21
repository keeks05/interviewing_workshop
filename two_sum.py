'''
Given an array of integers nums and an integer target, return the indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

You may return the answer in any order


Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Input: nums = []
target = 4
-1

nums = [1, 2], target = 4
return -1

Brainstorm:
    Brute Force:
        Time: O(n^2)
        Space: O(1)
    Hashmap w diffrence:
        Time: O(n)
        Space: O(n)

    Create hashmap
        value : index
    Iter thru nums
        Calc diff
        Check if hashmap contains diff
            return indexs
        Insert diff
    
    retutrn -1
'''

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    prev = {
            3: 0,
            2: 1,
            
            }
def two_sum(nums, target):
    prev_map = {} # value : index
    check = [['x'] fofr x]

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [i, prev_map[diff]]
        prev_map[num] = i
    return -1
