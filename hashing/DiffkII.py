class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        dic ={}
        for i in range(len(A)):
            if -B+A[i] in dic or B+A[i] in dic:
                return 1
            else:
                dic[A[i]] =i
                
        return 0
