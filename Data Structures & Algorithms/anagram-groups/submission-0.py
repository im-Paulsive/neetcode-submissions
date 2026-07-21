class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for a in strs:
            key=''.join(sorted(a))
            if key not in d:
                d[key]=[]
            d[key].append(a)
        return list(d.values())