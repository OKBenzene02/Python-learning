# Trie Data Structure - 23-03-17

# class Trie:
#     def __init__(self):
#         self.root = {"*": "*"}
#
#     def add_word(self, word):
#         curr_node = self.root
#         for letter in word:
#             if letter not in curr_node:
#                 curr_node[letter] = {}
#             curr_node = curr_node[letter]
#         curr_node['*'] = '*'
#
#     def does_word_exist(self, word):
#         cur_node = self.root
#         for letter in word:
#             if letter not in cur_node:
#                 return False
#             cur_node = cur_node[letter]
#         return '*' in cur_node
#
#     def startsWith(self, prefix):
#         cur_node = self.root
#         for letter in prefix:
#             if letter not in cur_node:
#                 return False
#             cur_node = cur_node[letter]
#         return True
#
#
# t = Trie()
#
# words = ["bad","dad","mad","pad","bad",".ad","b.."]
#
# for word in words:
#     t.add_word(word)
#
# print(t.does_word_exist("bad"))
# print(t.does_word_exist("mad"))
# print(t.does_word_exist(".ad"))
# print(t.does_word_exist('shop'))
# print(t.does_word_exist('hello'))

# ====================================================================
# Graph Traversals
# Breadth First Search and Depth First Search

# from collections import defaultdict
#
# class Graph:
#
#     def __init__(self):
#         self.graph = defaultdict(list)
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#     def bfs(self, s):
#         visited = [False] * (max(self.graph) + 1)
#         queue = []
#         queue.append(s)
#         visited[s] = True
#
#         while queue:
#             s = queue.pop(0)
#             print(s, end=" ")
#
#             for vertex in self.graph[s]:
#                 if visited[vertex] == False:
#                     queue.append(vertex)
#                     visited[vertex] = True
#
#     def dfsUtil(self, v, visited):
#         visited.add(v)
#         print(v, end=" ")
#
#         for vertex in self.graph[v]:
#             if vertex not in visited:
#                 self.dfsUtil(vertex, visited)
#
#     def dfs(self, v):
#         visited = set()
#         self.dfsUtil(v, visited)
#
#
#
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
#
# print("Following is Breadth First Traversal"
#       " (starting from vertex 2)")
# g.bfs(2)
# print()
# print("Following is Depth First Traversal"
#       " (starting from vertex 2)")
# g.dfs(2)

# ====================================================================

# Number of connections possible to make network connected

# from collections import deque, defaultdict
# class Connections:
#
#     def bfs(self, node, adj, visited):
#         queue = deque()
#         queue.append(node)
#         while queue:
#             node = queue.popleft()
#             for vertex in adj[node]:
#                 if not visited[vertex]:
#                     visited[vertex] = True
#                     queue.append(vertex)
#
#     def makeNetwork(self, n, adj):
#         if len(adj) < n - 1:
#             return -1
#
#         graph = defaultdict(dict)
#         for u, v in adj:
#             graph[u][v] = graph[v][u] = u
#
#         connected = 0
#         visited = [False] * n
#         for node in range(n):
#             if not visited[node]:
#                 self.bfs(node, graph, visited)
#                 connected += 1
#
#         return connected - 1
#
# network = Connections()
# print(network.makeNetwork(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
# ====================================================================

# Minimum score to a path between two cities

# from collections import defaultdict, deque
#
# class MinCost:
#
#     min_cost = 99999999999
#     def bfs(self, node, graph, n):
#         queue = deque()
#         queue.append(node)
#
#         visited = [False] * (n + 1)
#         visited[node] = True
#
#         while queue:
#             node = queue.popleft()
#             for vertex, score in graph[node].items():
#                 if not visited[vertex]:
#                     queue.append(vertex)
#                     visited[vertex] = True
#                 self.min_cost = min(self.min_cost, score)
#
#     def minCost(self, n: int, roads: list[list]):
#         graph = defaultdict(dict)
#
#         for u, v, w in roads:
#             graph[u][v] = graph[v][u] = w
#
#         self.bfs(1, graph, n)
#
#         return self.min_cost
#
#
# print(MinCost().minCost(4, [[1,2,2],[1,3,4],[3,4,7]]))

# ====================================================================
# Reorder Routes to Make All Paths Lead to the City Zero

# from collections import deque, defaultdict
#
# class Reorder:
#
#     reorder = 0
#     def bfs(self, node, graph, n):
#         queue = deque()
#         queue.append(node)
#
#         visited = [False] * n
#         visited[node] = True
#
#         while queue:
#             node = queue.popleft()
#             for vertex, sign in graph[node]:
#                 if not visited[vertex]:
#                     self.reorder += sign
#                     queue.append(vertex)
#                     visited[vertex] = True
#
#     def reOrder(self, n, paths):
#
#         graph = defaultdict(list)
#         for u, v in paths:
#             graph[u].append((v, 1))
#             graph[v].append((u, 0))
#
#         self.bfs(0, graph, n)
#
#         return self.reorder
#
#
#
# print(Reorder().reOrder(3, [[1,0],[2,0]]))

# ====================================================================

# Count Unreachable Pairs of Nodes in an Undirected Graph

# from collections import deque, defaultdict
#
# class Reorder:
#
#     def bfs(self, node, graph, visited):
#         queue = deque()
#         queue.append(node)
#
#         visited[node] = True
#
#         disconnected = 1
#         while queue:
#             node = queue.popleft()
#             for vertex in graph[node]:
#                 if not visited[vertex]:
#                     queue.append(vertex)
#                     visited[vertex] = True
#                     disconnected += 1
#         return disconnected
#
#     def reOrder(self, n, paths):
#
#         graph = defaultdict(list)
#         for u, v in paths:
#             graph[u].append(v)
#             graph[v].append(u)
#
#
#         visited = [False] * n
#         numberOfPairs, sizeOfComponent, remainingNodes = 0, 0, n
#         for vertex in range(n):
#             if not visited[vertex]:
#                 sizeOfComponent = self.bfs(vertex, graph, visited)
#                 numberOfPairs += sizeOfComponent * (remainingNodes - sizeOfComponent)
#                 remainingNodes -= sizeOfComponent
#
#         return numberOfPairs
#
#
# print(Reorder().reOrder(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]))
# ====================================================================
# Longest Cycle in a graph

# from collections import deque, defaultdict
#
# class LongestCycle:
#
#     ans = -1
#
#     def dfs(self, node, edges, dist, visited):
#         visited[node] = True
#         adj = edges[node]
#
#         if adj != -1 and not visited[adj]:
#             dist[adj] = dist.get(node) + 1
#             self.dfs(adj, edges, dist, visited)
#
#         elif adj != -1 and dist.get(adj):
#             self.ans = max(self.ans, dist.get(node) - dist.get(adj) + 1)
#
#     def longestCycle(self, edges):
#         n = len(edges)
#         visited = [False] * n
#         for vertex in range(n):
#             if not visited[vertex]:
#                 dist = {}
#                 dist[vertex] = 1
#                 self.dfs(vertex, edges, dist, visited)
#
#         return self.ans
#
#
# print(LongestCycle().longestCycle([3,3,4,2,3]))