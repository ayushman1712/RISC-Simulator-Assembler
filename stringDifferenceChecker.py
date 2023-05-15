f=open("himansusu.txt")
m=f.readlines()
f.close()
g=open("output.txt")
n=g.readlines()
g.close()
if m==n:
    print("sax sux")
else:
    print("no sax sux")