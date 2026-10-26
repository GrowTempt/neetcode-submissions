class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for index, word in enumerate(strs):
            sortedWord = ''.join(sorted(word))
    
            if sortedWord not in hashMap:
                hashMap[sortedWord] = [word]
            elif sortedWord in hashMap:
                hashMap[sortedWord].append(word)
 
        return list(hashMap.values())