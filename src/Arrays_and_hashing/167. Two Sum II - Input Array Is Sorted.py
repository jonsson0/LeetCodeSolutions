# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

 

# Constraints:

#     2 <= numbers.length <= 3 * 104
#     -1000 <= numbers[i] <= 1000
#     numbers is sorted in non-decreasing order.
#     -1000 <= target <= 1000
#     The tests are generated such that there is exactly one solution.



# Medium



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        





























# This problem is an extension to Two Sum problem. In the two-sum problem, the input array is unsorted and hence we have to use a hashmap to solve the problem in O(n) time. But that completely changes, once the input is sorted.
# The algorithm is:

#     Initialize two pointers i and j which points first and last element respectively.
#     Add elements pointed by i and j and then compare with target.
#     If target is smaller, it means you have added a larger element and it needs to be cut off. So we decrement j.
#     If target is larger, it means you have added a smaller value and we need to pick next big value. So we increment 'i`.
#     We repeat 2. and 3. until i>=j or a match is found.

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         i = 0
#         j = len(numbers) -1
        
#         while i<j:
#             s = numbers[i] + numbers[j]
#             if s == target:
#                 return [i + 1 , j + 1]
            
#             if s > target:
#                 j-=1
#             else:
#                i+=1 
        
#         return []

# Al_Dan pointed out that the solution can be made a bit more concise as the problem description states the following constraint:

#     The tests are generated such that there is exactly one solution.

# So instead of i<j check, we can do numbers[i] + numbers[j]!=target.

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         i = 0
#         j = len(numbers) -1
        
#         while numbers[i] + numbers[j]!=target:
#             s = numbers[i] + numbers[j]        
#             if s > target:
#                 j-=1
#             else:
#                i+=1 
        
#         return [i + 1 , j + 1]

# Time - O(n)
# Space - O(1)