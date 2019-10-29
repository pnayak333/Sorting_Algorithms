#Program - MergeSort

def merge(A):
    if len(A) <= 1:
        return A
    mid = int(len(A))//2
    left = merge(A[:mid])
    print("After Merge - Left: -Mid:",left)
    right = merge(A[mid:])
    print("After Merge - Right: - Mid", right)

    return merge_fun(left,right)

def merge_fun(left,right):
    result = []
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            print("Left - List Merged:",result)
            print('')
            i += 1

        else:
            result.append(right[j])
            print("Right - List Merged:",result)
            j += 1

    result += left[i:]
    result += right[j:]
    return result
lst = "Tact Cao"
lst = lst.lower()
#lst = [8,10,2,3,4,5,1,7,100]
#lst = ['z','a','x','c','v','b','n']
print(merge(lst))



