from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        algorithms:
            - brute force:
                - time complexity O(n*n)
                - space complexity O(1)
            - sorting:
                - time complexity O(nlogn)
                - space complexity O(1)
            - hash set:
                - time complexity O(n)
                - space complexity O(n)

        :param nums: list of int to verify if it contains duplicate
        :return: true if nums contain a duplicate else false
        """

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([10, 12, 20, 304, 53, 35, 1834]))
    print(solution.containsDuplicate([10, 12, 20, 304, 53, 23, 1834]))
    print(solution.containsDuplicate([10, 12, 20, 304, 53, 12, 1834]))
    print(solution.containsDuplicate([10, 12, 20, 304, 53, 1345, 1834, 10]))
