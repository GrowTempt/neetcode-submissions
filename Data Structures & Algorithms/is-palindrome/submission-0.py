class Solution:
    def isPalindrome(self, s:str) -> bool:
        filteredS = "".join(filter(str.isalnum, s)).lower()
        j = len(filteredS) - 1
        for i, charBeginning in enumerate(filteredS):
            if i >= j:
                break
            charEnding = filteredS[j]
            if charBeginning != charEnding:
                return False
            i += 1
            j -= 1
        return True
            
