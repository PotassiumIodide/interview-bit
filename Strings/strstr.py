class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if len(A)==0 or len(B)==0:
            return -1
        elif A==B:
            return 0
        else:
            n= len(B)
            for i in range(0,len(A)-n+1):
                if A[i:i+n]==B:
                    return i
            return -1
