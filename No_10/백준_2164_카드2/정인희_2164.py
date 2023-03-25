from collections import deque

n=int(input())
queue=deque()
for i in range(1,n+1):
    queue.append(i)

while len(queue)>1:
    x=queue.popleft()

    y=queue.popleft()

    queue.append(y)

print(queue[-1])