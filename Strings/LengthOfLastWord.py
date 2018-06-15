class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if len(A) == 0 :
            return 0
        i = len(A)-1
        count =0
        while(i !=-1):
            if A[i]==' ' and i== (len(A)-1):
                pass
            elif A[i]==' 'and count ==0:
                pass
            elif A[i]==' ':
                break
            else:
                count = count+1
            i =i-1
            
            
        return (count)
