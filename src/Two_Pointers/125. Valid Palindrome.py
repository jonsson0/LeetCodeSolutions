# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

 

# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.


import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)
        print(s)
        
        s2 = reversed(s)

        s2 = "".join(s2)
        
        if s == s2: 
            return True
        else: 
            return False



        
        
s = Solution()

s.isPalindrome("HEj123#")





































# Intuition

# The code aims to determine whether a given string is a palindrome or not. A palindrome is a string that reads the same forwards and backwards. The code uses two pointers, l and r, to traverse the string from the beginning and end simultaneously. It skips non-alphanumeric characters and compares the corresponding characters at l and r positions. If at any point the characters are not equal, the string is not a palindrome. If the pointers meet or cross each other, the string is a palindrome.
# Approach

#     Initialize l and r as the left and right pointers.
#     While l is less than r:
#         Increment l until it points to an alphanumeric character.
#         Decrement r until it points to an alphanumeric character.
#         If l becomes greater than r, return True as the string is a palindrome.
#         Compare characters at l and r (case-insensitive):
#             If they are not equal, return False as the string is not a palindrome.
#             If they are equal, increment l and decrement r.
#     Return True if the loop completes without finding any mismatch.

# Complexity

#     Time complexity: O(n)

#     Space complexity: O(1)

# Code

# Solution 1: (Two Pointers | Beats 99.99%)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l = 0
#         r = len(s) - 1
        
#         while l < r:
            
#             while l < r and s[l].isalnum() == False: 
#                 l += 1
#             while r > l and s[r].isalnum() == False: 
#                 r -= 1
#             if l > r or s[l].lower() != s[r].lower():
#                 return False
#             else:
#                 l += 1
#                 r -= 1
#         return True
                    

# Solution 2: (Simple two liner)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = [char.lower() for char in s if char.isalnum()]
#         return s == s[::-1]

# Please "Upvote" if you find it useful.