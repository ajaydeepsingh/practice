def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        
        banned = set(banned)
        
        for c in "!?',.;:":
            paragraph = paragraph.replace(c,' ')
            
        dictionary = {}
        res = ""
        count = 0
            
        for word in paragraph.lower().split():
            if word in banned:
                continue
            elif word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
            if dictionary[word] > count:
                count = dictionary[word]
                res = word
        
        return res