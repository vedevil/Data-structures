d=3
arr=[i for i in range(9)]
temp=arr[0:d]
for i in range(len(arr)-d):
    arr[i]=arr[i+d]
arr[-d:]=temp
print(arr)