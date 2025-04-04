from collections import deque

graph={'A':[('B',10),('C',15)],'B':[('D',12),('F',15)],'C':[('E',10)],'D':[('F',1),('E',2)],'F':[('E',5)]}

reverse_graph={}
for node in graph:
    for neighbor,cost in graph[node]:
        if neighbor not in reverse_graph:
            reverse_graph[neighbor]=[]
        reverse_graph[neighbor].append((node,cost))

def uniform_cost_search(start,goal):
    queue=[(0,start,[])]
    visited={}

    while queue:
        queue.sort()
        cost,node,path=queue.pop(0)

        if node in visited and visited[node]<=cost:
            continue
        visited[node]=cost
        path=path+[node]

        if node==goal:
            return path,cost

        for neighbor,edge_cost in graph.get(node,[]):
            queue.append((cost+edge_cost,neighbor,path))

    return None,float('inf')

def bidirectional_search(start,goal):
    if start==goal:
        return [start],0

    forward_queue=deque([(start,[start],0)])
    backward_queue=deque([(goal,[goal],0)])

    forward_visited={start:(0,[start])}
    backward_visited={goal:(0,[goal])}

    while forward_queue and backward_queue:
        f_node,f_path,f_cost=forward_queue.popleft()
        for neighbor,cost in graph.get(f_node,[]):
            new_cost=f_cost+cost
            if neighbor not in forward_visited or new_cost<forward_visited[neighbor][0]:
                forward_visited[neighbor]=(new_cost,f_path+[neighbor])
                forward_queue.append((neighbor,f_path+[neighbor],new_cost))

            if neighbor in backward_visited:
                total_cost=new_cost+backward_visited[neighbor][0]
                return f_path+backward_visited[neighbor][1][::-1][1:],total_cost

        b_node,b_path,b_cost=backward_queue.popleft()
        for neighbor,cost in reverse_graph.get(b_node,[]):
            new_cost=b_cost+cost
            if neighbor not in backward_visited or new_cost<backward_visited[neighbor][0]:
                backward_visited[neighbor]=(new_cost,[neighbor]+b_path)
                backward_queue.append((neighbor,[neighbor]+b_path,new_cost))

            if neighbor in forward_visited:
                total_cost=new_cost+forward_visited[neighbor][0]
                return forward_visited[neighbor][1]+backward_visited[neighbor][1][1:],total_cost

    return None,float('inf')

ucs_path,ucs_cost=uniform_cost_search('A','E')
bi_path,bi_cost=bidirectional_search('A','E')

print(f"OptimalPathusingUCS: {ucs_path} withCost:{ucs_cost}")
print(f"PathusingBi-DirectionalSearch: {bi_path} withCost:{bi_cost}")
