s={}
g={}
q=[]
for l in open(0):
 k=l.strip().split()
 if 'v'in k[0]:
  v,b=map(int,[k[1],k[-1]])
  if b in s:
   s[b].append(v)
   q.append(b)
  else:
   s[b]=[v]
 else:
  f=int(k[1])
  h='h'in k[3]
  a=('b'in k[5],int(k[6]))
  b=('b'in k[-2],int(k[11]))
  g[f]=[b,a]if h else[a,b]
p=1
while q:
 w=q.pop()
 if sorted(s[w])==[17,61]:print(w)
 for(a,b),x in zip(g[w],sorted(s[w])):
  if a:
   if b in s:
    s[b].append(x)
    q.append(b)
   else:
    s[b]=[x]
  elif b in[0,1,2]:
   p*=x
print(p)
