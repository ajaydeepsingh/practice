'''
Assume you have access to a function toss_biased() which returns 0 or 1 
with a probability that's not 50-50 (but also not 0-100 or 100-0). 
You do not know the bias of the coin.

'''
def tossUnbiased():
    val1 = toss_biased()
    val2 = toss_biased()

    if val1 == 0 and val2 == 1:
        return 0
    if val1 == 1 and val2 == 0:
        return 1

    return tossUnbiased();

    