#图结构散列表,记录每个节点和相邻节点的开销
graph = {}

graph['start'] = {}
graph['start']['a'] = 8
graph['start']['b'] = 5

graph['a'] = {}
graph['a']['b']= 2
graph['a']['c']= 1

graph['b'] = {}
graph['b']['e']= 4

graph['c'] = {}
graph['c']['d']= 2
graph['c']['g']= 6

graph['d'] = {}
graph['d']['e']= 0
graph['d']['f']= 1

graph['e'] = {}
graph['e']['f']= 1
graph['e']['h']= 2

graph['f'] = {}
graph['f']['fin']= 3
graph['f']['g']= 2

graph['g'] = {}
graph['g']['fin']= 7

graph['h'] = {}
graph['h']['fin']= 5

graph['fin'] = {}

#第二个散列表用于记录每个节点的父节点: 该散列表将不断更新
parents = {}
parents['start'] = None
parents['a'] = 'start'
parents['b'] = 'start'

#第三个散列表用于记录起点到每个节点的开销：该散列表将不断更新
infinit = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 8
costs['c'] = infinit
costs['d'] = infinit
costs['e'] = infinit
costs['f'] = infinit
costs['g'] = infinit
costs['h'] = infinit
costs['fin'] = infinit



#查找当前距离起点开销最少的节点
def find_lowest_cost_node(costs):
    lowest_cost_node = None
    lowest_cost = float('inf')
    for n in costs :
        if costs[n] < lowest_cost and n not in processed :
            lower_cost = costs[n]
            lowest_cost_node =  n
    return lowest_cost_node

#记录已经处理过的节点
processed =[]

#查找最短的路径

node = find_lowest_cost_node(costs)
#每次取出一个节点的邻居，计算到该邻居的开销是否更小，如果是，则更新该邻居的开销，并更新其父节点
while node is not None :
    #取出该节点的邻居节点集合
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = costs[node] + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

#获取最终路径的集合
chose_node = []
chose_node.append('fin')
f_node = parents['fin']
while f_node is not 'start':
     chose_node.append(f_node)
     f_node = parents[f_node]
     
chose_node.append('start')
chose_node.reverse()

print(costs)
print(parents)        
print(chose_node)
print(costs['fin'])

 