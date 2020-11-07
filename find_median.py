# Dan Wu
# 11/3/2020
# Write a function named find_median that takes a list of numbers and it returns the median of those numbers.




def find_median(some_num):
    some_num.sort()

    if(len(some_num) %2 == 1):
        return some_num[len(some_num)//2]
    else:
        return (some_num[len(some_num) // 2-1] + some_num[len(some_num) // 2])/2


