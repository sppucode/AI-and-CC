graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red','Green','Blue']
assignment= {}
nodelist = list(graph.keys())

print(nodelist)

def is_valid(graph,node,color,assignment):
    for i in graph[node]:
        if i in assignment and assignment[i] == color:
            return False
    return True

def solve(graph,colors,assignment,node_list,index=0):
    if index == len(node_list):
        return assignment
    
    node = node_list[index]

    for color in colors:
        if is_valid(graph,node,color,assignment):
            assignment[node] = color
            result = solve(graph,colors,assignment,node_list,index + 1)
            if result:
                return result
            assignment.pop(node)
    return None

solution = solve(graph,colors,assignment,nodelist)
if solution:
    print("coloring solution : ")
    for region,color in solution.items():
        print(region," : ",color)
else:
    print("No solution found")




