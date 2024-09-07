import logging
import networkx as nx

nxl = logging.getLogger("networkx")
handler = logging.StreamHandler()
nxl.addHandler(handler)
nxl.setLevel(logging.DEBUG)

graph = nx.erdos_renyi_graph(100, 0.5)
out = nx.betweenness_centrality(graph)

print("first", out[0])
