class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lums = len(nums)
        pre = [1] * lums
        pos = [1] * lums
        answer = nums
        for i in range(1,lums) :
            pre[i] = nums[i-1] * pre[i-1]
        for i in range(lums-2,-1,-1):
            pos[i] = pos[i+1] * nums[i+1]
        for i in range(1,lums-1):
            answer[i] = pre[i] * pos[i]
        answer[0] = pos[0]
        answer[lums-1] = pre[lums-1]
        print(answer)
a = Solution()
b = [1,2,3,4]
a.productExceptSelf(b)
