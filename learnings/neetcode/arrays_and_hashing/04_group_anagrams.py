from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            Given an array of strings strs, group the anagrams together. You can return the answer in any order.
            An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
            typically using all the original letters exactly once.

        :param strs:
        :return:
        """
        res = defaultdict(List)  # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26  # a....z
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # output : [["bat"],["nat","tan"],["ate","eat","tea"]]

    print(solution.groupAnagrams([""]))
    # output : [[""]]

    print(solution.groupAnagrams(["a"]))
    # output : [["a"]]
