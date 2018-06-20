class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n =len(A)
        if len(A)==0 or len(A)==1:
            return len(A)
        
        count = 1
        k=0
        for i in range(len(A)-1):
            if A[i]==A[i+1]:
                if count==1:
                    A[k]=A[i]
                    count+=1
                    k+=1
                elif count >2:
                    count +=1
            if A[i] !=A[i+1]:
                if count==1 or count==2:
                    A[k]=A[i]
                    k+=1
                    count =1
                if count >2:
                    count =1
            
        A[k]=A[n-1]
        k+=1
        return k
