class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i =0
        j=1
        while i <len(A) and j<len(A) :
            if A[j]-A[i]==B and j!=i:
                return 1
            elif A[j]-A[i]>B:
                i+=1
            else:
                j+=1
        return 0
