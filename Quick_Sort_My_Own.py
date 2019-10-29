def quick(A,low,high):
    #if len(A) <=1:
        #return A
    if low < high:
    #P = Get_Pivot(A,low,high)
        Pi =Partition(A,low,high)
        quick(A,low,Pi -1)
        quick(A,Pi +1,high)

def Partition(A,low,high):
    #P = A[Pi]
    mid = (low + high) // 2
    Pi = high
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            Pi = mid
    elif A[low] < A[high]:
        return Pi
    i = (low -1)
    for j in range(low,high+1):
        if A[j] <= i:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[Pi] = A[Pi],A[i+1]
    return (i+1)

def Get_Pivot(A,low,high):
    mid = (low+high) // 2
    Pi = high
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            Pi = mid
    elif A[low] < A[high]:
        Pi = low
    return Pi




lst = [10,1,5,90,100,12,9]
n = len((lst))
quick(lst,0,n-1)
for i in range(n):
    print(lst[i])