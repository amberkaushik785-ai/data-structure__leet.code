def slidingwindow(nums,w):
    current=0
    for i in range (w):
        current=current+nums[i]

    max_window=current
    for j in range (1,len(nums)-w+1):
        current=current-nums[j-1]+nums[j+w-1]

        if current > max_window :
            max_window=current

    return max_window


nums=[3,8,2,5,7,6,12]
w=4
print(slidingwindow(nums,w))