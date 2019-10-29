#Program - MergeSort
def Quick_Sort(Arr,low,high):
    if low < high:
        Pi = Partition(Arr,low,high)
        Quick_Sort(Arr,low,Pi-1)
        Quick_Sort(Arr,Pi+1,high)
def Partition(Arr,low,high):
    i = (low -1)
    Pivot = Arr[high]
    for j in range(low,high):
        if Arr[j] <= Pivot:
            i +=1
            Arr[i],Arr[j] = Arr[j],Arr[i] # Checking and Adding Smaller elements to the left of the Pivot
    Arr[i+1],Arr[high] = Arr[high],Arr[i+1] #Swapping last indexof i with Pivot
    return (i+1) #Retuning Index of the Pivot

#lst = [10,1,3,4,2,11]
lst = ['e','a','t']
n = len(lst)
Quick_Sort(lst,0,n-1)
for i in range(n):
    print(lst[i])



