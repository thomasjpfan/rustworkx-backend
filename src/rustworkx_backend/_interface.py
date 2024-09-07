from ._converter import _filter_expected_values, _convert_dict_to_values
from ._graph import (
    _convert_rustworkx_to_networkx,
    RustworkXGraph,
)
import networkx as nx
import rustworkx as rx


class BackendInterface:
    # Centrality
    betweenness_centrality = _filter_expected_values(
        rx.betweenness_centrality, nx.betweenness_centrality, _convert_dict_to_values
    )

    @staticmethod
    def convert_from_nx(graph, *args, **kwargs):
        if isinstance(graph, RustworkXGraph):
            return graph
        return RustworkXGraph(graph)

    @staticmethod
    def convert_to_nx(result, *, name=None):
        if isinstance(result, RustworkXGraph):
            return _convert_rustworkx_to_networkx(result)
        return result
