#Shun Fai Lee Lab4
def insertionsort(nums: list):
    cp = 1
    ex = 0
    for i in range(1 , len(nums)):
        temp = nums[i]
        j = i
        while nums[j-1] > temp and j > 0:
            cp += 1
            nums[j] = nums[j-1]
            j = j - 1
            ex += 1
        nums[j] = temp
        ex += 1
    return nums, cp, ex