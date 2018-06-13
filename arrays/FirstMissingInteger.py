class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        res = 1
        A = set(a for a in A if a > 0)
        while res in A:
            res += 1
        return res
