def max_gain(input_list):
    
    small = input_list[0]
    gain = 0
    
    for x in input_list:
        if x < small:
            small = x
        
        if (x - small > gain):
            gain = x - small

    return gain
# Driver Code

print(max_gain([100,40,20,10])) # 0
print(max_gain([0,50,10,100,30])) # 100