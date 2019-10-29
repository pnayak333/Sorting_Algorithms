#Program - Sorting Compate i to all elements

mylst = [4,5,1,2,-1,10,3,100]
#mylst = ['z','v','c','a','e','r','b']
l = len(mylst)
#print(l)
def BubbleSort(mylst):
    for i in range(0,(len(mylst)-1)):
        for j in range(0,(len(mylst)-1-i)):
       # first = mylst[j]
       # sec = mylst[j]
            if mylst[j] > mylst[j+1]:
                mylst[j],mylst[j+1] = mylst[j+1],mylst[j]
                #temp = mylst[j]
                #mylst[j] = mylst[j+1]
                #mylst[j+1] = temp
    return mylst

#for i in mylst:
print(BubbleSort(mylst))