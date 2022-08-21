
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

visited={}
level={}
parent={}
queue=[]

for node in adjDict.keys():
   visited[node]=False
   level[node]=-1
   parent[node]=None


root_node="A"
visited[root_node]=True
level[root_node]=0

queue.append(root_node)
bfs_traversal_output=[]
dfs_traversal_output=[]

while len(queue)!= 0:
  root_node=queue.pop()
  bfs_traversal_output.append(root_node)
  for node in adjDict[root_node]:
     if visited[node]==False:
        visited[node]=True
        level[node]=level[root_node]+1
        parent[node]=root_node
        queue.append(node)

path=[]
tn="F"

while tn:
   path.append(tn)
   tn=parent[tn]

path.reverse()

print("##### B.F.S ####")
print(bfs_traversal_output)
print(path)


#D.F.S

for node in adjDict.keys():
   visited[node]=False
   level[node]=-1
   parent[node]=None

def dfs(root_node):
   dfs_traversal_output.append(root_node)
   for node in adjDict[root_node]:
     if visited[node]==False:
        visited[node]=True
        parent[node]=root_node
        level[node]=level[root_node]+1
        dfs(node)


root_node="A"
visited[root_node]=True
level[root_node]=0
dfs(root_node)

path=[]
tn="F"
while tn:
   path.append(tn)
   tn=parent[tn]
path.reverse()

print("\n#### D.F.S ####")
print(dfs_traversal_output)
print(path)

