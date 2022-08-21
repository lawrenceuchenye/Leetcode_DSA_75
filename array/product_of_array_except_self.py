
def parray(arr,rm_indx):
    new_arr=[ i for i in arr if i != arr[rm_indx] ] 
    product=1
    for num in new_arr:
      product=product*num
    return product



arr=[-1,1,0,-3,3]
print([parray(arr,i) for i in range(len(arr))])
