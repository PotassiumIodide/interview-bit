class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxSubArray(self, A):
	    max_so_far = A[0]
	    max_ending_here = A[0]
	    for i in range(1,len(A)):
	        max_ending_here =max(A[i],max_ending_here+A[i])
	        max_so_far =max(max_so_far,max_ending_here)
	            
	    return max_so_far
