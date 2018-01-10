import string

string=raw_input("dose string" )
p=list(string)
x=len(p)
for  i in range (x):
    if chr(ord(p[i]))<chr(ord("n")):
       p[i]=chr(ord(p[i]) +13)
    else:
        p[i]=chr(ord(p[i]) -13)
final=''.join(p)
print final