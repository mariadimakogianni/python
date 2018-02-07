import random
bingo = ['b','b','b','b','b']
arithmoi=[]
for m in range (1000):
    k=0
    paiktes = []
    for i in range (100):
         paiktis = []
         while len(paiktis)<5:
            x=random.randint(1, 80)
            if x not in paiktis:
                paiktis.append(x)
         paiktes.append(paiktis)
    noep=[]
    while bingo not in paiktes:
        y=random.randint(1,80)
        if y not in noep:
            k=k+1
            noep.append(y)
            for i in range(100):
                for j in range(5):
                    if y == paiktes[i][j]:
                        paiktes[i][j]="b"
    arithmoi.append(k)
lsum=sum(arithmoi)
mo= lsum/1000.0
print 'o mesos oros arithmon pou prepei na anagkelthoyn gia na ginei bingo einai' ,mo