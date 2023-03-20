# 균형잡힌 세상
while True:
    s = input()
    bracket = []
    if s == '.':
        break
    for ch in s:
        if ch == '(':
            bracket.append(ch)
        elif ch == '[':
            bracket.append(ch)
        elif ch == ')':
            if len(bracket) > 0:
                if bracket[-1] == '(':
                    bracket.pop()
                else:
                    break
            else:
                bracket.append('no')
        elif ch == ']':
            if len(bracket) > 0:
                if bracket[-1] == '[':
                    bracket.pop()
                else:
                    break
            else:
                bracket.append('no')

    if len(bracket) == 0:
        print("yes")
    else:
        print("no")

