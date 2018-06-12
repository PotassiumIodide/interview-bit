class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
    
    #The idea here is to first sort the 
    #given array and then interchange the 
    #two consecutive digits like index
    # 0 and 1 will be swipped and 2 and 3 
    #will be swipped
        A =list(sorted(A))
        for i in range(0,len(A)-1,2):
            temp = A[i]
            A[i]= A[i+1]
            A[i+1] = temp 
        return A
