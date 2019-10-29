#Nth largest like N=2

def Max_Elements(A,n):
    result = []
    for sizeof_N in range(0,n):
        max = 0
        for j in range(0,len(A)):
            if A[j] > max:
                max = A[j]

        A.remove(max)
        result.append(max)
    return result

lst = [10,2,44,5,9,11,100]

n = 3

print(Max_Elements(lst,n))