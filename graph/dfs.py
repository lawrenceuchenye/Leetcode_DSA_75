
"""
  A @@@ B      C     H
  @ @          @     @
  @  @         @     @
  @    @       @     @
  D @@@ E @@@@ F @@@ G
"""


#graph dict
adjDict={
    "A":["B","E","D"],
    "B":["A"],
    "C":["F"],
    "D":["A","E"],
    "E":["D","A","F"],
    "F":["E","C","G"],
    "G":["F","H"],
    "H":["G"]
  }


adjDict={
    "A":["G","B"],
    "B":["C","G"],
    "C":["B"],
    "G":["J","E"],
    "J":["D","F"],
    "D":["J","F"],
    "E":["G","K"],
    "F":["D","J"],
    "K":["E"]
}



visited={}
explored={}
parent={}
level={}

dfs_traversal_output=[]
queue=[]

for node in adjDict.keys():
   visited[node]=False
   parent[node]=None
   level[node]=-1
   explored[node]=False

print(visited)
print(explored)
print(parent)
print(level)

s="A"
level[s]=None
queue.append(s)

def has_next(pn,val):
   print((pn,val))
   dfs_traversal_output.append(pn)
   if visited[pn]==False and len(val)==1:
      visited[pn]=True
      return val
   for node in val:
      return has_next(node,adjDict[node])

def traverse(pn):
   if visited[pn]==False:
     dfs_traversal_output.append(pn)
     visited[pn]=True
     for subnode in adjDict[pn]:
        if explored[subnode]==False:
           explored[subnode]=True
           parent[subnode]=pn
        traverse(subnode)

traverse(s)
parent[s]=None
target_node="F"

tmp_target_node=target_node

path=[]

while tmp_target_node:
  path.append(tmp_target_node)
  tmp_target_node=parent[tmp_target_node]

path.reverse()
print("Root_node:{},Target_node:{}".format(s,target_node))
print("Path:",path)
print("Traversed:",dfs_traversal_output)

