#Program - Normal Sorting
#Program - Sorting Compate i to all elements

mylst = [4,5,1,2,10,-1,-10,100]
#mylst = ['z','v','c','a','e','r','b']
l = len(mylst)
#print(l)
def BubbleSort(mylst):
    for i in range(0,(len(mylst)-1)):
        for j in range(i,(len(mylst)-1)):
       # first = mylst[j]
       # sec = mylst[j]
            if mylst[i] > mylst[j+1]:
                mylst[i],mylst[j+1] = mylst[j+1],mylst[i]
                #temp = mylst[j]
                #mylst[j] = mylst[j+1]
                #mylst[j+1] = temp
    return mylst

#for i in mylst:
print(BubbleSort(mylst))