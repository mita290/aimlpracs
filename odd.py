n=int(input())
arr=[]
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
for i in range(0,n):
    if arr[i]%2!=0:
        arr[i]=-1
print(arr)