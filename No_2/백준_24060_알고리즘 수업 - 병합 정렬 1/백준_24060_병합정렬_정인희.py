
def merge_sort(p,r):
    if p<r:
        q=(p+r)//2
        #print('q',q)
        merge_sort(p,q)
        merge_sort(q+1,r)
        merge(A,p,q,r)

result=[]

def merge(A,p,q,r):
    # print('in merge p,q r',p,q,r)
    tmp=[]
    i=p
    j=q+1
    while i<=q and j<=r:
        if A[i]<A[j]:
            tmp.append(A[i])
            result.append(A[i])
            i+=1
        else:
            tmp.append(A[j])
            result.append(A[j])
            j+=1
    while i<=q:
        tmp.append(A[i])
        result.append(A[i])
        i+=1

    while j<=r:
        tmp.append(A[j])
        result.append(A[j])
        j+=1
    i=p
    while i<=r:
        A[i]=tmp[i-p]
        i+=1

n,k=map(int,input().split())

A=list(map(int,input().split()))

merge_sort(0,len(A)-1)

# print('tmp',tmp)
# print(A)
# print('result',result)

if k<=len(result):
    print(result[k-1])

else:
    print(-1)