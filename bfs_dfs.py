graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['G','H'],
    'D':['F'],
    'E':[''],
    'F':[''],
    'G':[''],
    'H':['']
}

# BFS 
visited =[]
queue = []

def B_F_S(visited,graph,node):
    visited.append(node)
    queue.append(node)


    while queue:
        m = queue.pop(0)
        print(m)
        for i in graph[m]:
            if i and i not in visited:
                visited.append(i)
                queue.append(i)


print("Breadth First Solution : ")
B_F_S(visited,graph,'A')


# DFS
print("depth First Search ")
node='A'
visited = []
def dfs(visited,graph,node):
    visited.append(node)
    print(node)
    for i in graph[node]:
        if i and i not in visited:
            dfs(visited,graph,i)

dfs(visited,graph,'A')
