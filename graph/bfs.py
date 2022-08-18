from queue import Queue


"""

  B @@@ A    E @@@ G

  @     @   @       @
  @     @  @ @      @
  @     @ @  @      @

  C     D @@@ F @@@ H

"""

#Node/Vertex dict
adjDict={
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["H","E"],
    "G":["E","H"],
    "H":["F","G"]
 }


#bfs code

visited={}
level={}
parent={}
bfs_traversal_output=[]
queue=[]


#map adjDict
for node in adjDict.keys():
   visited[node]=False
   level[node]=-1
   parent[node]=None


#main bfs code
#source node

s="A"
visited[s]=True
level[s]=0

queue.append(s)
while not len(queue)==0:
  u=queue.pop()
  bfs_traversal_output.append(u)
  for v in adjDict[u]:
    if not visited[v]:
       visited[v]=True
       parent[v]=u
       level[v]=level[u]+1
       queue.append(v)
       
print(bfs_traversal_output)
	
v="F"
path=[]
while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()
print(path)
