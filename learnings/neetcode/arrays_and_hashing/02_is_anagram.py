class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        algorithms:

        :param s: first input string
        :param t: second string to validate if it is an anagram of s
        :return: true if t is anagram of s else false
        """
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('anagram', 'nagaram'))
    print(solution.isAnagram('rat', 'car'))

