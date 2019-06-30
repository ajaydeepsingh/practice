def LongestWord(sen):


    # remove non-alph characters
    notvalid = [';',':','"','<','.','?','!','@','#','$','%','^','&','*','(',')']
    sen = sen.translate(None,''.join(notvalid))

    words = sen.split(' ')

    longest = ''

    for x in words:
        if len(x) > len(longest):
            longest = x
        elif len(x) == len(longest):
            pass

    # code goes here
    return longest

# keep this function call here
print(LongestWord(raw_input())
