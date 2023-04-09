import queue
import math

class Node:
    id = -1
    pai = None
    
    def __init__(self,id):
        self.id = id
        self.custo = 0
    
    def __lt__(self, other):
        return self.custo < other.custo

class Grafo:
    
    matriz = []
    n = 0
    direcionado = False
    
    def __init__(self,n,direcionado): 
        self.n = n
        self.direcionado = direcionado
        for i in range(n):
            self.matriz.append([0]*n)            
    
    def addAresta(self,s,t):
        if(not self.direcionado):
            self.matriz[t][s]=1
        self.matriz[s][t]=1
        
    def printMatriz(self):
        print()
        print('##########')
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j],end = ' ')
            print()
        print('##########')
        print()
    
    def bl(self,s,t):
        q = queue.Queue()
        
        node = Node(s)
        node.pai = Node(-1)       
        
        q.put(node)
        
        while(not q.empty()):
            aux = q.get()
            
            # Teste de Objetivo           
            if(aux.id == t):
                return aux
            # Teste de Objetivo
            
            # Expansão de vizinhos            
            for i in range(self.n):                
                if(self.matriz[aux.id][i] == 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    q.put(node)
            # Expansão de vizinhos
        
        return aux
        
    def bp(self,s,t):
        stack = []
        
        node = Node(s)
        node.pai = Node(-1)       
        stack.append(node)
        
        while(len(stack) > 0):
            aux = stack.pop()
            
            # Teste de Objetivo           
            if(aux.id == t):
                return aux
            # Teste de Objetivo
            
            # Expansão de vizinhos            
            for i in reversed(range(self.n)):                
                if(self.matriz[aux.id][i] == 1 and i != aux.pai.id):
                    node = Node(i)
                    node.pai = aux
                    stack.append(node)
            # Expansão de vizinhos
            
        return aux

    def bcu(self,s,t):
        pq = queue.PriorityQueue()
        
        node = Node(s)
        node.pai = Node(-1)
        node.custo = 0
        pq.put(node)
        
        while not pq.empty():
            aux = pq.get()
            
            # Teste de Objetivo           
            if aux.id == t:
                return aux
            # Teste de Objetivo
            
            # Expansão de vizinhos            
            for i in range(self.n):                
                if self.matriz[aux.id][i] == 1 and i != aux.pai.id:
                    node = Node(i)
                    node.pai = aux
                    node.custo = aux.custo + 1
                    pq.put(node)
            # Expansão de vizinhos
            
        return aux
        
    def bme(self, s, t):
        pq = queue.PriorityQueue()
    
        node = Node(s)
        node.pai = Node(-1)
        node.custo = 0
        pq.put(node)
    
        while not pq.empty():
            aux = pq.get()
    
            # Teste de Objetivo
            if aux.id == t:
                return aux
            # Teste de Objetivo
    
            # Expansão de vizinhos
            vizinhos = []
            for i in range(self.n):
                if self.matriz[aux.id][i] == 1 and i != aux.pai.id:
                    vizinhos.append(Node(i))
                    vizinhos[-1].pai = aux
                    vizinhos[-1].custo = self.h(i, t))
    
            # Ordena os vizinhos pela heurística
            vizinhos.sort(key=lambda x: x.custo)
            
            for vizinho in vizinhos:
                pq.put(vizinho)
            # Expansão de vizinhos
    
        return aux
    
        
    def a_estrela(self,s,t):
        pq = queue.PriorityQueue()
        
        node = Node(s)
        node.pai = Node(-1)
        node.custo = 0
        pq.put(node)
        
        while not pq.empty():
            aux = pq.get()
            
            # Teste de Objetivo           
            if aux.id == t:
                return aux
            # Teste de Objetivo
            
            # Expansão de vizinhos            
            for i in range(self.n):                
                if self.matriz[aux.id][i] == 1 and i != aux.pai.id:
                    node = Node(i)
                    node.pai = aux
                    node.custo = aux.custo + 1 + self.h(i, t)
                    pq.put(node)
            # Expansão de vizinhos
            
        return aux        
        
    def h(self, s, t):
        # heurística
        xi, yi = s % 5, s // 5
        xf, yf = t % 5, t // 5
        return math.sqrt((xf - xi) ** 2 + (yf - yi) ** 2)

g = Grafo(10,False)

g.printMatriz()

g.addAresta(0, 2)
g.addAresta(1, 3)
g.addAresta(2, 3)
g.addAresta(3, 5)
g.addAresta(5, 4)
g.addAresta(3, 6)
g.addAresta(6, 9)
g.addAresta(4, 7)
g.addAresta(4, 8)
g.addAresta(8, 9)

g.printMatriz()

objetivo = g.bme(0, 9)
   
while(objetivo.id != -1):
    print(objetivo.id)
    objetivo = objetivo.pai
