def Sort_Array(A,low,high):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(A[j] > A[j+1]):
                A[j],A[j+1] = A[j+1],A[j]
    return A


def Search(A,low,high,key):
    if low <= len(A)-1:

        mid = (low+high) // 2
        if A[mid] == key:
            print( key,"Found - Mid")
        elif key < A[mid]:
            Binary_Low_Mid(A,low,mid-1,key)
        elif key > A[mid]:
            Binary_High_Mid(A, mid+1,high, key)
        else:
            print("Not Found",key)
                    #Not_Found(A,low,high,key)

def Binary_Low_Mid(A,low,mid,key):
    for num in range(low,mid+1):
        if A[num] == key:
            print(key,"Found : < Mid")

def Binary_High_Mid(A, mid,high, key):
    for num in range(mid, high+1):
        if A[num] == key:
            print(key, "Found: > Mid")


def Not_Found(A,low,high,key):
    for num in range(low,high+1):
        if A[num] != key:
            print("Not in Liost")
result = []
lst = [-1,2,55,44,3,100,10,21]
n = len(lst)
#print(n)
result = Sort_Array(lst,0,n-1)

for i in range(len(result)):
    print(result[i])

l = len(result)
num = int(input("Enter The Key to Search -"))
Search(result,0,l-1,num)