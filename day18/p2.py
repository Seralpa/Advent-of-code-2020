def collapse(operation):
    aux=[]
    partial_sum=0
    for i, c in enumerate(operation):
        if c=='+':
            if partial_sum==0:
                partial_sum=int(operation[i-1])+int(operation[i+1])
            else:
                partial_sum+=int(operation[i+1])
        elif c=='*':
            if partial_sum!=0:
                aux.append(partial_sum)
                partial_sum=0
                aux.append('*')
            else:
                aux.append(int(operation[i-1]))
                aux.append('*')
    if operation[-2]=='*':#add last num if num is a mult
        aux.append(operation[-1])
    if partial_sum!=0:
        aux.append(partial_sum)

    result=int(aux[0])
    for i, c in enumerate(aux):
        if c=='*':
            result*=int(aux[i+1])
    return result

with open('day18/input.txt') as f:
    operations=[list(l) for l in f.read().replace(' ', '').splitlines()]
answer=0
for op in operations:
    op.insert(0, '(')
    op.append(')')
    opening_pars=0
    while '(' in op:
        for i, c in enumerate(op):
            if c=='(':
                opening_pars=i
            elif c==')':
                partial=collapse(op[opening_pars+1:i])
                for j in reversed(range(opening_pars, i+1)):
                    op.pop(j)
                op.insert(opening_pars, partial)
                break
    answer+=op[0]
    # print(op[0])
print(answer)