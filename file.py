from itertools import count


f = open('Bio.txt', 'r+')
f2= open('Bio.txt','r')
count=0
for i in f:
    x=i.replace(" ","_").strip()
    count+=1
    a=f"{x}={count}"
    print(a+ '\n')
    fp=open('Bio.txt','w')
    fp.write('first line')
    fp.close()