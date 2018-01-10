import random
bingo = ['b','b','b','b','b']
arithmoi=[]
for m in range (1000):
    k=0
    paiktis = []
    for i in range (100):
        num = []
        for j in range (5):
            x=random.randint(1, 80)
            num.append(x)
        paiktis.append(num)
    while bingo not in paiktis:
        k=k+1
        y=random.randint(1,80)
        for i in range(100) :
         for j in range(5):
          if y == paiktis[i][j]:
              paiktis[i][j]="b"
    arithmoi.append(k)
lsum=sum(arithmoi)
mo= lsum/1000
print 'o mesos oros arithmon pou prepei na anagkelthoyn gia na ginei bingo einai' ,mo