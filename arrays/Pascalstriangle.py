class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        arr = []
        for i in range(A):
            arr.append([])
        
        for i in range(0,A):
            for j in range(0,i+1):
                if(i==j or j==0):
                    arr[i].append(1)
                else:
                    
                    arr[i].append(arr[i-1][j]+arr[i-1][j-1])
        return arr
