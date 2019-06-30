def is_power_of_four(number):
    if len(bin(number))%2 == 0:
        return False
    else:
        return True


print(is_power_of_four(1024))
print(is_power_of_four(2048))
print(is_power_of_four(1))
print(is_power_of_four(12))
