# BRUTE-FORCE METHOD 
def twosum(arr,target):

  for i in range(len(arr)):

    for j in range(i+1,len(arr)):

      if arr[i]+arr[j]==target:

        return [i,j]

arr=[2,6,5,8,11]
target=14

print(twosum(arr,target))
