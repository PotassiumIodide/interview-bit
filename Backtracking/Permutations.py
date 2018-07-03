class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    
    def helper(self,A,chosen,arr):
        if len(A)==0:
            arr.append(chosen[:])
        else:
            for i in range(len(A)):
                c =A[i]
                chosen.append(c)
                del(A[i])
                self.helper(A,chosen,arr)
                A.insert(i,c)
                del(chosen[-1])
        
    def permute(self, A):
        arr =[]
        self.helper(A,[],arr)
        return arr
        
