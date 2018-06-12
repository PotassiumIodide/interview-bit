class Solution:
     # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        nrows = len(A)
        ncols = len(A[0])
        for x, row in enumerate(A):
            if 0 in row:
                for y, n in enumerate(row):
                    if n == 0: 
                        A[0][y] = None
                    if n != 0 or x != 0:
                        A[x][y] = 0
        for i in range(nrows):
            i_ = nrows - i -1
            for j in range(ncols):
                if A[0][j] is None:
                    A[i_][j] = 0
                            
        return A
