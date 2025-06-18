#write a code to delete the dupliicate values in the list
# Using dict.fromkeys
nums = [1,1,2]
corrector_nums=list(dict.fromkeys(nums))
print(corrector_nums)

# Using set()
nums = [1,1,2]
corrector_nums=list(set(nums))
print(corrector_nums)