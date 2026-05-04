class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphnumericS = ""
        for char in s:
            if char.isalnum():
                alphnumericS += char.lower()
        return alphnumericS == alphnumericS[::-1]
