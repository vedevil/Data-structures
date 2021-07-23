def findpivot(left,right,arr):
    while left!=right:
        mid=(right+left)//2
        if arr[mid]>arr[right]:
            left=mid+1
        else:
            right=mid
    return arr[left],left

arr=[7,9,11,12,5]
print(findpivot(0, len(arr)-1, arr)[1])