class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strslist = {}
        for word in strs:
            letterlist = [0] * 26
            for st in word:
                letterlist[ord(st) - ord('a')] += 1
            letterlist = tuple(letterlist)
            if letterlist in strslist:
                strslist[letterlist].append(word)
            else:
                strslist[letterlist] = [word]
        return list(strslist.values())