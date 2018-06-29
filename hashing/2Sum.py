class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        dic = {}
        
        for i in range(len(A)):
            diff = B - A[i]
            if diff not in dic:
                if A[i] not in dic:
                    dic[A[i]] = i+1
            else:
                return [dic[diff] , i+1]
        
        return [
