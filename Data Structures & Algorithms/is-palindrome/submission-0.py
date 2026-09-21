class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(filter(str.isalnum, s))
        s = s.lower()
        s_list = list(s)
        print(s_list)

        # pointer 1
        p1 = 0

        # pointer 2
        p2 = len(s) - 1

        if len(s_list) == 1:
            return True
        
        while p1 <= p2:
            if s_list[p1] != s_list[p2]:
                return False
            p1 = p1 + 1
            p2 = p2 - 1
        
        return True
            