class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}   # Step 1: create an empty dictionary

        for i, num in enumerate(nums):  # Step 2: loop through list with both index and value
            complement = target - num   # Step 3: calculate what number we need
            if complement in num_to_index:  # Step 4: check if we've seen it before
                return [num_to_index[complement], i]  # Step 5: return indices
            num_to_index[num] = i  # Step 6: store this number and its index
