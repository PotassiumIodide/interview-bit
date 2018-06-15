class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        curWord = ''
        listOfWords = []
        for char in A :
            if char != ' ' :
                curWord += char
            else :
                if curWord != '' :
                    listOfWords.append(curWord)
                curWord = ''
        if curWord != '' :
            listOfWords.append(curWord)
        listOfWords.reverse()
        return " ".join(word for word in listOfWords)
