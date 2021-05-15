def validPalindrome(self, s: str) -> bool:
    if s == s[::-1]:
        return True
    for i in range(len(s) - 1):
        if s[i] != s[~i]:
            return s[i: -i - 2] == s[i + 1: -i - 1][::-1] or s[i + 1: -i - 1] == s[i + 2: len(s) - i][::-1]
    return False

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'