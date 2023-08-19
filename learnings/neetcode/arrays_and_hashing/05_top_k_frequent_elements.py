from typing import List


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order.

        :param nums:
        :param k:
        :return:
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    # output : [1,2]

    print(solution.top_k_frequent([1], 1))
    # output : [1]
