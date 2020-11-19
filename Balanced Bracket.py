N='[{[({}[[([])]])]}]'
brackets={'}':'{',']':'[',')':'('}
open=['{','[','(']
close=['}',']',')']
l=[]
m=0
for i in N:
    if i in open:
        l.append(i)
    elif i in close:
        if l:
            a=l.pop()
            if(a==brackets[i]):
                continue
            else:
                m+=1
                break
        else:
            m+=1
            break
    else:
        m=10
        break
if m==10:
    print("Invalid Expression")
elif(m!=0 or l):
    print("Brackets are not Balanced")
else:
    print("Brackets are Balanced")