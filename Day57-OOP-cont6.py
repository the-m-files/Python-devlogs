#-----------------------------#
#          TWO SUM            #
#-----------------------------#

# Today I worked on the Two Sum problem from LeetCode.
#
# The goal:
# Find two numbers in a list that add up to the target
# and return their indexes.
#
# I already knew how to solve this using brute force:
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             return i, j
#
# This works, but it checks lots of combinations.
#
# Today I started learning a faster appro   ach using a dictionary.
#
# The main idea is to store:
#
#       number -> index
#
# Then, while looping through the list:
#
# 1. Take the current number.
# 2. Calculate the number needed to reach the target.
# 3. Check if that number has already been seen.
# 4. If it has, return the two indexes.
# 5. If it hasn't, remember the current number and its index.
#
# Example:
#
# nums = [2, 7, 11, 15]
# target = 9
#
# Start with 2:
#
# needed = 9 - 2
# needed = 7
#
# If 7 has already been seen, we have found the pair.
#
# I also learned why using .index() can cause problems:
#
# nums.index(value)
#
# always finds the FIRST occurrence of that value.
# This can cause problems when the list contains duplicates,
# such as:
#
# nums = [3, 3]
#
# So instead of searching for indexes afterward,
# the better idea is to remember the indexes while looping.
#
# Main thing I learned today:
#
#       value -> index
#
# and using a dictionary to remember values I've already seen.
#
# I didn't completely finish implementing the optimized version,
# but I understand the core idea behind it.