class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        for item in zip(*strs):
            if len(set(item)) == 1:
                prefix.append(item[0])
            else:
                break
        return ''.join(prefix)
