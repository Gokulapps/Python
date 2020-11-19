def largensmall(num):
    f=[]
    t=num
    while t>0:
        digit=t%10
        t=t//10
        f.append(digit)
    return max(f),min(f)

def significant_digit(number):
    t=number
    while(t>0):
        digit=t%10
        t=t//10
    return digit

def trunc(input):
    temp=input
    count=0
    sum=""
    while temp>0 and count<2:
        digit=temp%10
        temp=temp//10
        sum=str(digit)+sum
        count+=1
    return int(sum)

#Start
l=[8,234,567,321,345,123,110,767,111]
print('Original List:',l)
res=[]
for i in l:
    if(i>10):
        a,b=largensmall(i)
        a*=11
        b*=7
        bit_score=a+b
        bit_score=trunc(bit_score)
        res.append(bit_score)
print('Bit Score:',res)
final=[]
for i in res:
    final.append(significant_digit(i))
print('Single Digit:',final)
s=[]
count1=0
sum=0
for i in range(0,len(final),2):
    if final[i] in s:
        count1+=1
    else:
        s.append(final[i])
print('Odd Pair:',count1)
count2=0
s2=[]
for i in range(1,len(final),2):
    if final[i] in s2:
        count2+=1
    else:
        s2.append(final[i])
print('Even Pair:',count2)
sum+=(count1+count2)
print('Final Pair:',sum)






