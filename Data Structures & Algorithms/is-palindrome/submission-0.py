class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(i for i in s if i.isalnum()).lower()
        return st == st[::-1]