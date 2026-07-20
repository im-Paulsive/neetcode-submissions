class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        a=set(nums)
        a=sorted(a)
        if a!=nums:
            return True
        else:
            return False