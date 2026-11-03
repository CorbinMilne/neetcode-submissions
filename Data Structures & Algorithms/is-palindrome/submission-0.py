import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        lower = cleaned.lower()
        

        l, r = 0, len(lower) - 1

        while l <= r:
            if lower[l] != lower[r]:
                return False

            l += 1
            r -= 1

        return True 

        