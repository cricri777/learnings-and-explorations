from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        algorithms:
            - brute force:
                - time complexity: O(n*n)
                - space complexity: O(1)
            - hashmap:
                - time complexity: O(n)
                - space complexity: O(n)
        :param nums: list of integer
        :param target: integer
        :return: the indices of the two numbers such that they add up to target
        """

        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i, hashmap[diff]]
            else:
                hashmap[n] = i


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([1, 2, 3, 4, 5, 6], 10))
    print(solution.twoSum([1, 2, 3, 4, 5, 5], 10))
