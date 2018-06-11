class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        #since the elements of the tuples are
        #in range of length of tuple, all elements
        #if taken as index is valid.
        for i in range(len(A)):
            if(A[abs(A[i])] >= 0):
                A[abs(A[i])] = -A[abs(A[i])]
            else:
                return abs(A[i])
