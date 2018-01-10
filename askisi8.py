import random
ran=[0]*30
for i in range (30):
    ran[i]=random.randint(-30,30)
p=0
for i in range (30):
  for j in range (30):
    for k in range(30):
      if i!=j and j!=k and k!=i:
         if ran[i]+ran[j]+ran[k]==0:
           print (ran[i],ran[k],ran[j])
           p=1
if p==0:
    print("den yparxei tetoia triada")