import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum, s)).lower()
        end = len(new_s) - 1
        for i in range(0, len(new_s) // 2):
            if new_s[i] != new_s[end - i]:
                return False
        return True
