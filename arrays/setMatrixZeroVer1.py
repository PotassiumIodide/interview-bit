class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        
        m = len(A[0])
        n = len(A)
        list_row = []
        list_col = []
        
        for i in xrange(n):
            for j in xrange(m):
                if A[i][j] == 0:
                    if i not in list_row:
                        list_row.append(i)
                    if j not in list_col:
                        list_col.append(j)
        #print list_row, list_col
        row = [0]*m
        
        for i in xrange(n):
            if i in list_row:
                A[i] = row
            for j in xrange(m):
                if j in list_col:
                    A[i][j] = 0
            
        return A
