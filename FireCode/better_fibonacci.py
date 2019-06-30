def better_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    previous1 = 0
    previous2 = 1
    total = previous1 + previous2
    for x in range(2,n+1):
        total = previous1 + previous2
        previous1 = previous2
        previous2 = total
    
    return total



# driver code

# print(better_fibonacci(0))
# print(better_fibonacci(1))
# print(better_fibonacci(3))
for x in range(40):
    print(x, better_fibonacci(x))