
nums=[1,2,3]

def containsDuplicate(arr):
   hashmap={}
   for num in arr:
     if num not in hashmap:
       hashmap[num]=num
     else:
       return True
   return False

print(containsDuplicate(nums))
