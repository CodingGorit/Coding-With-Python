def BoubleSort(lists):
    length=len(lists)
    for i in range(0,length):
        for j in range(i+1,length):
            if(lists[i]>lists[j]):
                lists[i],lists[j]=lists[j],lists[i]

    return lists

def BoubleSort1(li):
    for i in range(0,len(li)):
        flag = 0
        for j in range(i+1,len(li)):
            if li[i]>li[j]:
                li[i],li[j] = li[j],li[i]
                flag = 1
        if flag == 0:
            break

li=[2,4,5,3,1]
BoubleSort1(li)
print(len(li),li)