graph={'A':{'B':10,'C':15},
       'B':{'D':12,'F':15},
       'C':{'E':10},
       'D':{'F':1,'E':2},
       'F':{'E':5},
       'E':{}
       }
def dijkstra(graph,start):
 u=set(graph.keys())
 s={n:float('inf')for n in graph}
 s[start]=0
 p={n:[]for n in graph}
 p[start]=[start]
 while u:
  c=min(u,key=lambda n:s[n])
  if s[c]==float('inf'):break
  u.remove(c)
  for n,w in graph[c].items():
   nc=s[c]+w
   if nc<s[n]:s[n]=nc
   p[n]=p[c]+[n]
 return s,p
def bfs(graph,start):
 v=set()
 q=[start]
 t=[]
 while q:
  n=q.pop(0)
  if n not in v:
   v.add(n)
   t.append(n)
   q.extend(graph[n].keys())
 return t
def dfs(graph,start,v=None):
 if v is None:
  v=set()
  v.add(start);t=[start]
  for n in graph[start]:
   if n not in v:t.extend(dfs(graph,n,v))
  return t
def has_cycle(graph):
 v=set()
 r=set()
 def dfs_cycle(n):
  if n in r:
   return True
  if n in v:
   return False
  v.add(n)
  r.add(n)
  for ne in graph[n]:
   if dfs_cycle(ne):
    return True
  r.remove(n)
  return False
 for n in graph:
  if n not in v:
   if dfs_cycle(n):
    return True
 return False
def graph_coloring(graph,mx=3):
 c={}
 for n in graph:
  ac=set(range(mx))
  for ne in graph[n]:
   if ne in c:ac.discard(c[ne])
  c[n]=min(ac)
 return c
s,p=dijkstra(graph,'A')
bfs_t=bfs(graph,'A')
dfs_t=dfs(graph,'A')
cyc=has_cycle(graph)
col=graph_coloring(graph)
print("Shortest Paths from A:",s)
for n in p:print(f"Path to {n}: {' -> '.join(p[n])}")
print("\nBFS Traversal:"," -> ".join(bfs_t))
print("DFS Traversal:"," -> ".join(dfs_t))
print("\nCycle Detection:",cyc)
print("Graph Coloring:",col)









