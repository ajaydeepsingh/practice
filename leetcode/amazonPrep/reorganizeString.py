from heapq import *

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        
        # find freq of all letters
        
        # take most freq, pop, readd most freq
        
        freqDict = dict()
        
        for letter in s:
            if letter in freqDict:
                freqDict[letter] += 1
            else:
                freqDict[letter] = 1
        
        
        maxHeap = []
        
        for letter, frequency in freqDict.items():
            heappush(maxHeap, (-frequency, letter))
            
        
        result = []
        previousLetter = None
        previousCount = 0
        while maxHeap:
            frequency, letter = heappop(maxHeap)
            result.append(letter)
            frequency = frequency + 1
            if previousCount != 0:
                heappush(maxHeap, (previousCount, previousLetter))
            previousCount = frequency
            previousLetter = letter
        
        result = ''.join(result)
        
        return result if len(result) == len(s) else ''