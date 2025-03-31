import heapq

class MinimaxAlphaBeta:
    def __init__(self):
        self.pruned_nodes=0  

    def minimax(self,node,depth,alpha,beta,maximizingPlayer,graph):
        if isinstance(graph[node],int):  
            return graph[node],[node]

        children=graph[node]
        heap=[]

        
        for child in children:
            value=graph[child] if isinstance(graph[child],int) else 0
            heapq.heappush(heap,(-value if maximizingPlayer else value,child))

        if maximizingPlayer:
            max_eval=float('-inf')
            best_path=[]
            while heap:
                _,child=heapq.heappop(heap)  
                eval,child_path=self.minimax(child,depth-1,alpha,beta,False,graph)
                if eval>max_eval:
                    max_eval=eval
                    best_path=[node]+child_path
                alpha=max(alpha,eval)
                if beta<=alpha:
                    self.pruned_nodes+=1
                    break  
            return max_eval,best_path
        else:
            min_eval=float('inf')
            best_path=[]
            while heap:
                _,child=heapq.heappop(heap)  
                eval,child_path=self.minimax(child,depth-1,alpha,beta,True,graph)
                if eval<min_eval:
                    
                    min_eval=eval
                    best_path=[node]+child_path
                beta=min(beta,eval)
                if beta<=alpha:
                    self.pruned_nodes+=1
                    break  
            return min_eval,best_path


figure1_graph={
    'A':['B1','B2','B3'],
    'B1':['C1','C2','C3'],
    'B2':['C4','C5','C6'],
    'B3':['C7','C8','C9'],
    'C1':12,'C2':10,'C3':3,
    'C4':5,'C5':8,'C6':10,
    'C7':11,'C8':2,'C9':12
}

figure2_graph={
    'MAX':['MIN1','MIN2'],
    'MIN1':['MAX1','MAX2'],
    'MIN2':['MAX3','MAX4'],
    'MAX1':['L1','L2'],
    'MAX2':['L3','L4'],
    'MAX3':['L5','L6'],
    'MAX4':['L7','L8'],
    'L1':5,'L2':-1,'L3':4,'L4':3,
    'L5':2,'L6':4,'L7':7,'L8':-3
}
solver1=MinimaxAlphaBeta()
optimal_value1,path1=solver1.minimax('A',3,float('-inf'),float('inf'),True,figure1_graph)
print("Figure 1:")
print("Optimal Value:",optimal_value1)
print("Optimal Path:", " -> ".join(path1))
print("Pruned Nodes:",solver1.pruned_nodes)

solver2=MinimaxAlphaBeta()
optimal_value2,path2=solver2.minimax('MAX',3,float('-inf'),float('inf'),True,figure2_graph)
print("\nFigure 2:")
print("Optimal Value:",optimal_value2)
print("Optimal Path:", " -> ".join(path2))
print("Pruned Nodes:",solver2.pruned_nodes)


