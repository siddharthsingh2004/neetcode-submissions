class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Make into list
        s_list = list(s)
        t_list = list(t)

        if sorted(s_list) == sorted(t_list):
            return True
        return False



