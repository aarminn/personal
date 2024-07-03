class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split()
        ss.reverse()
        print(' '.join(ss))
        return ' '.join(ss)
        
a = Solution()

a.reverseWords('    hello     world')