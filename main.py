# checks for the first missing number in array
def check_array(num):
    # check if array only contains numbers less than zero
    if max(num) > 0 or min(num) > 0:
        # loop through from 1 to max value in array
        for x in range(1, max(num) + 1):
            # check if the number is in the array
            if x in num:
                # check if loop reaches the max value
                if x == max(num):
                    return x + 1
                continue
            else:
                return x
    else:
        return 1


numbers = [-2, 5, 12, 7, 1, 3, -4, 2, 6, 8]
print(check_array(numbers))