class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(str)
        dict_t = defaultdict(str)
        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1
        for i in t:
            if i not in dict_t:
                dict_t[i] = 1
            else:
                dict_t[i] += 1
        return dict_s == dict_t
        