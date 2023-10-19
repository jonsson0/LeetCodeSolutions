# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

 

# Constraints:

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.

 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


# Medium


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        





































# !! BIG ANNOUNCEMENT !!
# I am currently Giving away my premium content well-structured assignments and study materials to clear interviews at top companies related to computer science and data science to my current Subscribers. This is only for first 10,000 Subscribers. DON'T FORGET to Subscribe
# Search 👉 Tech Wired Leetcode to Subscribe
# Video Solution
# Search 👉 Top K Frequent Elements by Tech Wired
# or
# Click the Link in my Profile
# Approach:

#     Create a counter to count the frequency of each element in the input list.
#     Use a min heap to keep track of the k most frequent elements.
#     Iterate over the counter's items:
#     Push each element into the heap along with its frequency.
#     If the heap size exceeds k, pop the smallest element from the heap.
#     Extract the k most frequent elements from the heap and store them in a result list.
#     Return the result list.

# Intuition:

#     We start by counting the frequency of each element in the input list using a counter. This allows us to efficiently determine the frequency of each element in O(n) time, where n is the number of elements in the list.
#     By using a min heap, we can keep track of the k most frequent elements while maintaining the order of elements with the smallest frequency at the top of the heap.
#     We iterate over the counter's items and push each element into the heap along with its frequency. If the heap size exceeds k, we pop the smallest element, ensuring that we only keep the k most frequent elements in the heap.
#     After iterating through all the elements, the heap will contain the k most frequent elements in ascending order of frequency. We extract these elements from the heap and store them in a result list.
#     Finally, we return the result list, which contains the k most frequent elements in the desired order.

# class Solution:
#     def topKFrequent(self, nums, k):
#         counter = Counter(nums)
#         heap = []
        
#         for num, freq in counter.items():
#             heapq.heappush(heap, (-freq, num))
        
#         result = []
#         for _ in range(k):
#             result.append(heapq.heappop(heap)[1])
        
#         return result