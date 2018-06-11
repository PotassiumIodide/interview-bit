class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        a =[]
        for i in range(len(A)):
            if A[i] not in a and i==len(A)-1:
                return -1
            elif A[i] in a:
                return A[i]
            else:
                a.append(A[i])
