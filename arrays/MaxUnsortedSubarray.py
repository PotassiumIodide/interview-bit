class Solution:
	# @param A : list of integers
	# @return a list of integers
	def subUnsort(self, A):
	    sortA =list(sorted(A))
	    start =len(A)
	    end =0
	    for i in range(len(A)):
	        if A[i]!=sortA[i]:
	            start = min(i,start)
	            end =max(end,i)
        
        if start-end == len(A):
            return [-1]
        else:
            return [start,end]
