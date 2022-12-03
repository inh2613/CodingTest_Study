

def hanoi(k,start,mid,end):
    if k==0:
        return
    hanoi(k-1,start,end,mid)

    print(start,end)
    hanoi(k-1,mid,start,end)


k=int(input())
print(2**k-1)

hanoi(k,1,2,3)