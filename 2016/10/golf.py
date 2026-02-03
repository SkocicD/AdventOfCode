s=[[]for _ in range(999)]
o=list.append
g={}
q=[]
for l in open(0):
 z=l.split()
 k=[int(x)for x in z if x[0]<'a']
 if len(k)<3:
  v,b=k
  if len(s[b]):o(q,b)
  o(s[b],v)
 else:a=('b'in z[5],k[1]);b=('b'in z[-2],k[2]);g[k[0]]=[b,a]if 'h'in z[3] else[a,b]
p=1
while q:
 w=q.pop()
 if [17,61]==(z:=sorted(s[w])):print(w)
 for(a,b),x in zip(g[w],z):
  if a:
   if len(s[b]):o(q,b)
   o(s[b],x)
  elif b<3:p*=x
print(p)
