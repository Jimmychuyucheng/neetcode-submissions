class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_hash = {}
        for str in strs:
            sorted_str = sorted(str)
            sorted_key = "".join(sorted_str)
            if sorted_key not in ans_hash:
                ans_hash[sorted_key] = []
            ans_hash[sorted_key].append(str)
        return list(ans_hash.values())

        