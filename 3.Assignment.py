#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]

num=[1,2,3,4,5,6,7]
k=3
num[:]=num[-k:]+num[:-k]
print(num)