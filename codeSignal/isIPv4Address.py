def isIPv4Address(inputString):

    x = inputString.split('.')

    if len(x) != 4:
        return False

    for o in x:
        try:
            if not ((0 <= int(o)) and (int(o) <= 255)):
                return False
        except:
            return False


    return True


