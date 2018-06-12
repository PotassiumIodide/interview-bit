class Solution:
	# @param A : list of integers
	# @return a list of integers
	def maxset(self, A):
	    i = 0;
        maxi = -1;
        index = 0;
        a = []
        l=[]
        
        for i in range(len(A)):
            if A[i] < 0:
                l = []
            if A[i] >= 0:   
                l.append(A[i])
            
            if (sum(l) > maxi):
                a = l
                maxi = sum(l)
        
        return a
