import random
ran=[0]*30
lis=[]
prod=[]
for i in range (30):
    ran[i]=random.randint(-30,30)
p=0
for i in ran:
  for j in ran:
    for k in ran:
      if i!=j and j!=k and k!=i:
         if i+j+k==0:
           pr=[i,j,k]
           gin = i*j*k
           if not gin in prod:
               prod.append(gin)
               lis.append(pr)
           p=1
if p==0:
    print("den yparxei tetoia triada")
else:
    print lis
