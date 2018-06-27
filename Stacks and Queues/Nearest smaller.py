class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack =[]
        arr=[]
        for i in range(0,len(A)):
            while len(stack)!=0 and stack[-1]>=A[i]:
                    stack.pop()
            if len(stack)==0:
                arr.append(-1)
            else:
                arr.append(stack[-1])
            stack.append(A[i])
            
        return arr
                
        
