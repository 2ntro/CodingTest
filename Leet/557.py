class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        splits = s.split()
        for split in splits:
            result.append(split[::-1])
        return ' '.join(result)
    