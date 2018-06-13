class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        temp =0
        for i in range(len(A)):
            for j in range(i,len(A)):
                temp =A[i][j]
                A[i][j]= A[j][i]
                A[j][i] =temp
                
        if len(A)%2==0:
            for i in range(len(A)):
                for j in range((len(A)/2)):
                    temp =A[i][j] 
                    A[i][j] =A[i][len(A)-j-1]
                    A[i][len(A)-j-1] =temp
        elif len(A)%2!=0:
            for i in range(len(A)):
                for j in range((len(A)+1)/2):
                    temp =A[i][j] 
                    A[i][j] =A[i][len(A)-j-1]
                    A[i][len(A)-j-1] =temp
        return A
