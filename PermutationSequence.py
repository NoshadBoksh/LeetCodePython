import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]  # available digits
        k -= 1  # convert to 0-indexed
        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result.append(nums[index])
            nums.pop(index)
            k %= fact

        return "".join(result)
