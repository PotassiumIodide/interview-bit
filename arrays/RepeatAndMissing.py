class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        arr =[0]*(len(A)+1)
        for i in range(len(A)):
            arr[A[i]]=arr[A[i]]+1
        
        for i in range(1,len(arr)):
            if arr[i]==0:
                missing = i
            if arr[i]==2:
                repeat =i
        
        return[repeat,missing]
