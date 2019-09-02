"""
Given an array nums containing n + 1 integers where each integer is between 1 
and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

"""



def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    check1 = nums[0]
    check2 = slow
    
    while check1 != check2:
        check1 = nums[check1]
        check2 = nums[check2]
        
    return check1