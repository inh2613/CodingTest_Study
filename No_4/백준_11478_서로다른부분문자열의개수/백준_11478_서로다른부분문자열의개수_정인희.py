
s=input()
result=[]

for i in range(1,len(s)+1,1):
    for j in range(len(s)):
        result.append(s[j:i])

result=set(result)

print(len(result)-1)


