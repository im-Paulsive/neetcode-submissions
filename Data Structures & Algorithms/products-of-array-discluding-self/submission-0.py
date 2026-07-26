class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        res=[0]*n
        prefix[0]=1
        suffix[n-1]=1
        for _ in range(1,n):
            prefix[_]=nums[_-1]*prefix[_-1]
        for _ in range(n-2,-1,-1):
            suffix[_]=nums[_+1]*suffix[_+1]
        for _ in range(n):
            res[_]=suffix[_]*prefix[_]
        return res