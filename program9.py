# leetcode problem 4
def medianofsortedarray(arr1,arr2):
    arr=arr1+arr2
    sorted(arr)
    if len(arr) % 2 ==0:
        return (arr[len(arr)//2]+arr[ len(arr)//2 - 1])/2

    else:
        return arr[len(arr)//2]


arr1=[1,2,3]
arr2=[4,5] 
print(medianofsortedarray(arr1,arr2))       