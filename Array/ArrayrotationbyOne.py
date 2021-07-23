arr=[i for i in range(1,7)]
for i in range(len(arr)):
    temp=arr[i-1]
    arr[i-1]=arr[i]
    arr[i]=temp
print(arr)