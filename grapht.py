from collections import deque

gra = {
    0:["8","1","5"],
    1:["0"],
    5:["0","8"],
    8:["0","5"],
    2:["3","4"],
    3:["2","4"],
    4:["3","2"]
}


def largets(graph,k,vis):
    if k in vis:
        return False
    
    vis.add(k)
  
    b = 1
    
    for neightbor in graph[k]:
        b += largets(graph,int(neightbor),vis)
    return b
        
    
    
    
    
    
    
    
big = 0
visited = set()
for k in gra.keys():
    big += largets(gra,int(k),visited) 
    
print(big)
