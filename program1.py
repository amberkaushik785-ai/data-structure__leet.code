def sorting(arr, type):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):

            if type == 'asc':
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

            elif type == 'desc':
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

    return arr
arr=[2,9,5,8,3,1,7]
type='asc'
print(sorting(arr,type))