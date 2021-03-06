# checks for the first missing number in list
def check_list(num):
    # check if array only contains numbers less than zero
    if max(num) > 0 or min(num) > 0:
        # loop through from 1 to max value in list
        for x in range(1, max(num) + 1):
            # check if the number is in the list
            if x in num:
                # check if loop reaches the max value
                if x == max(num):
                    return x + 1
                continue
            else:
                return x
    else:
        return 1

# best on performance 
def solution(A):
   a=frozenset(sorted(A))
   m=max(a)
   if m>0:
       for i in range(1,m):
           if i not in a:
              return i
       else:
          return m+1
   else:
       return 1

numbers = [-2,  12, 7, 1, 3, -4, 2, 6, 8]
print(check_list(numbers))
