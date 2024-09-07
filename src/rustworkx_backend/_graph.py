import rustworkx as rx
import networkx as nx


def _convert_rustworkx_to_networkx(graph):
    edge_list = [
        (graph[x[0]], graph[x[1]], {"weight": x[2]}) for x in graph.weighted_edge_list()
    ]

    if isinstance(graph, rx.PyGraph):
        if graph.multigraph:
            return nx.MultiGraph(edge_list)
        else:
            return nx.Graph(edge_list)
    else:
        if graph.multigraph:
            return nx.MultiDiGraph(edge_list)
        else:
            return nx.DiGraph(edge_list)


class RustworkXGraph:
    __networkx_backend__ = "rustworkx"

    def __init__(self, graph_object=None):
        if graph_object is None:
            self.graph_object = rx.PyGraph()
        elif isinstance(graph_object, (rx.PyGraph, rx.PyDiGraph)):
            self.graph_object = graph_object
        else:
            self.graph_object = rx.networkx_converter(graph_object)

    def __str__(self):
        return str(self.graph_object)
