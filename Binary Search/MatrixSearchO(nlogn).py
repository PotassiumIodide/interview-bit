class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        for i in range(len(A)):
            start =0
            end = len(A[i])-1
            while(start<=end):
                mid = (start+end)/2
                if B ==A[i][mid]:
                    return 1
                elif B<A[i][mid]:
                    end =mid-1
                else:
                    start =start+1
        return 0
