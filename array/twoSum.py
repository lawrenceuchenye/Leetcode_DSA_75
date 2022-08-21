
arr=[3,2,4,2]

#### unoptimal ####
def two_sum(target):
    target_arr=[]
    for n in range(len(arr)):
      for j in range(len(arr)):
        if((arr[n]==target - arr[j]) and (n != j)):
            target_arr.append([n,j])
            return target_arr
    return target_arr



def two_sum_hashmap(target):
   hashmap={}
   for i in range(len(arr)):
     mp=target-arr[i]
     if mp in hashmap:
         return [i,hashmap[mp]]
     hashmap[arr[i]]=i

