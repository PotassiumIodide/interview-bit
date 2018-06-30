class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(A)):
            if A[i] in usedChar and start <= usedChar[A[i]]:
                start = usedChar[A[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[A[i]] = i

        return maxLength
