def solution(n):
    answer=0
    i=1
    while True:
        number=str(i)
        for num in number:
            answer+=int(num)
        answer+=i
        if answer==n:
            return i
        else:
            i+=1
            answer = 0
        if i>=n:
            #print(answer)
            return 0

    #print(answer)
    return i


n=int(input())

print(solution(n))