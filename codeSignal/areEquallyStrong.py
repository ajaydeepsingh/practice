def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    
    if yourLeft + yourRight == friendsLeft + friendsRight:
        if yourLeft == friendsLeft or yourLeft == friendsRight:
            if yourRight == friendsLeft or yourRight == friendsRight:
                return True
    
    return False
            

