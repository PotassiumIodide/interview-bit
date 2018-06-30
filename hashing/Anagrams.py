class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
	    dic =dict()
	    for i in range(len(A)):
	        string =A[i]
	        temp =''.join(sorted(string))
	        if dic.get(temp,0)==0:
	            dic[temp]=[]
	            dic[temp].append(i+1)
            else:
                dic[temp].append(i+1)
        return list(dic.values())
