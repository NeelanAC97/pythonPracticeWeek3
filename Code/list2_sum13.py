""" Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6 """

def sum13(nums):

  sum = 0
  
  for n in nums:
    
    if n == 13:
      if nums.index(13) < len(nums)-1:
        nums.pop(nums.index(n)+1)
    else:
      sum += n
      
  return sum