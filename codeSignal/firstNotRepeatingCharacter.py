"""
Given a string s consisting of small English letters, find and return 
the first instance of a non-repeating character in it. If there is no 
such character, return '_'.
"""

def firstNotRepeatingCharacter(s):
    seen = set()
    d = {}
    for i,x in enumerate(s):
        if x not in seen:
            d[x] = i
            seen.add(x) 
        elif x in d:
            del d[x]
    return min(d, key=d.get) if d else '_'