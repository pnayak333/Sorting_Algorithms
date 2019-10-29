lst = [10,1,2,5,3,6]

def m(A):
    devide(A,0,len(A)-1)

def devide(A,first,last):
    if first < last:
        middle = (first,last) // 2
        print(middle)