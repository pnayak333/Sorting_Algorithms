
def Insertion_Sort(Arr,n):
    if len(Arr) <=1:
        return Arr
    for i in range(1,len(Arr)):
        j=i
        while(j>0 and Arr[j-1] > Arr[j]):
            Arr[j-1],Arr[j] = Arr[j], Arr[j-1]
            j-=1
    return Arr

lst = [100,1,22,55,33,23,99]
n = len(lst)-1
Insertion_Sort(lst,n)
for i in range(len(lst)):
    print(lst[i])