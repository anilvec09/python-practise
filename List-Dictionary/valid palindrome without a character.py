class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, i, j, replacedCount):
            if j <= i:
                return True

            if s[i] == s[j]:
                return isPalindrome(s, i + 1, j - 1, replacedCount)

            if replacedCount >= 1:  # one replacement has been made already
                return False

            if isPalindrome(s, i + 1, j, replacedCount + 1):
                return True
            return isPalindrome(s, i, j - 1, replacedCount + 1)


        return isPalindrome(s, 0, len(s) - 1, 0)