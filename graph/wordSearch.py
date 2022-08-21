
wordTable=[
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

word="ABCCED"
path=[]

def dfs(r,c,i):
   if i == len(word):
      return True
  
   if( ((r,c) in path) or ( r < 0 or c < 0 or r >= len(wordTable) or c >= len(wordTable[0])) or word[i] != wordTable[r][c]):
     return False
   path.append((r,c))
   res=( dfs(r+1,c,i+1) or
         dfs(r-1,c,i+1) or
         dfs(r,c+1,i+1) or
         dfs(r,c-1,i+1)  )
   return res
  


for r in range(len(wordTable)):
  for c in range(len(wordTable[0])):
     if dfs(r,c,0):
        print("Found",path)
        break
