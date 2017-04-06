class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_dic = {}
        for idx, num in enumerate(nums):
            if num not in num_dic:
                num_dic[num] = [idx]
            else:
                if [i for i in num_dic[num] if idx - i <= k] != []:
                    return True
                num_dic[num].append(idx)
        return False
