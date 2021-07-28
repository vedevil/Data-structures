#arr=[11, 13, 21, 3]
#arr=[4, 5, 2, 25]
#arr=[13, 7, 6, 12]
arr=[6,8,0,1,3]
ans=dict()
stack=[arr[0]]
for i in range(1,len(arr)):
    if len(stack)==0:
        stack.append(arr[i])
    elif arr[i]>stack[-1]:
        while len(stack)!=0 and arr[i]>stack[-1]:
            a=stack.pop()
            ans[a]=arr[i]
        stack.append(arr[i])
    else:
        stack.append(arr[i])
while len(stack)!=0:
    ans[stack.pop()]=-1
for e in arr:
    print(str(e)+'-----> '+str(ans[e]))