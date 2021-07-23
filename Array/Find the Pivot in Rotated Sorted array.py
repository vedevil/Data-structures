def findpivot(left,right,arr):
    while left!=right:
        mid=(right+left)//2
        if arr[mid]>arr[right]:
            left=mid+1
        else:
            right=mid
    return arr[left]

arr=[10,20]
print(findpivot(0, len(arr)-1, arr))

