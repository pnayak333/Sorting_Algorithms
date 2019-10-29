#Lienear Search

def Lienear_Search(A,low,high,num):
    for i in range(low,high+1):
        if A[i] == num:
            found = True
            #print("Hurrrreee ! The Key Found in the", i, "th position of  List :", A[i])
            break
            #continue
            #return num
            #print(A[i],"- Hurrreeee!Key Found ",)
        else:
            found = False
            #print("Not Found the Key")
    if (found == True):
        print("Hurrrreee ! The Key Found in the",i,"th position of  List :",A[i])
    else:
        print("Opppps Key Not Found!")
found = False
lst = [10,21,1,111,2,66,3,10]
print("List:",lst)
num = int(input("Enter the Key to Search:"))
Lienear_Search(lst,0,len(lst)-1,num)