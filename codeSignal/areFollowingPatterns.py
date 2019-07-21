"""
Given an array strings, determine whether it follows the sequence given in the 
patterns array. In other words, there should be no i and j for which strings[i] 
= strings[j] and patterns[i] != patterns[j] or for which strings[i] != strings[j]
 and patterns[i] = patterns[j].


"""
def areFollowingPatterns(strings, patterns):

    # pattern_dict = {}

    # for i, v in enumerate(patterns):
    #     if v in pattern_dict:
    #         pass
    #     if strings[i] in pattern_dict.values():
    #         return False
    #     else:
    #         pattern_dict[v] = strings[i]


    # for i, v in enumerate(patterns):
    #     if pattern_dict.get(patterns[i]) != strings[i]:
    #         return False

    # return True

    for s,p in zip(S,P):
        if P.index(p) != S.index(s): return False
    return True





strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]

print(areFollowingPatterns(strings, patterns))
