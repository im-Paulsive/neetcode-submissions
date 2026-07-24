class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for _ in nums:
            if _ not in d:
                d[_]=1
            d[_]+=1

        top=[key for key,value in sorted(d.items(), key=lambda x:x[1], reverse=True)[:k]]
        return top