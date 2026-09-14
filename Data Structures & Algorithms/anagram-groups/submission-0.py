class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        for i in range(len(strs)):
            sorted_list.append(''.join(sorted(strs[i])))

        hashmap = {}

        for idx, val in enumerate(sorted_list):
            if val in hashmap:
                hashmap[val].append(strs[idx])
            else:
                hashmap[val] = [strs[idx]]
        return_list = []
        for val in hashmap:
            return_list.append(hashmap[val])
        return return_list
        