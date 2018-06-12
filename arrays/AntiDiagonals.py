class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        arr = []
        for i in range(len(A)):
            diag =[]
            for j in range(0,i+1):
                diag.append(A[j][i-j])
            arr.append(diag)
        for i in range(len(A), 2*len(A)-1):
            diag =[]
            for j in range(i-len(A)+1,len(A)):
                diag.append(A[j][i-j])
            arr.append(diag)
            
        return arr
