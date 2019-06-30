def FirstFactorial(num):

    # code goes here
    if num < 2:
        return 1
    else:
        return num * FirstFactorial(num-1)

# keep this function call here
print(FirstFactorial(8))
