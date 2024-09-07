__all__ = ["get_info"]


def get_info():
    return {
        "backend_name": "rustworkx",
        "project": "rustworkx-backend",
        "package": "rustworkx-backend",
        "url": "https://github.com/thomasjpfan/rustworkx-backend",
        "short_summary": "A networkx backend that is a thin wrapper around rustworkx",
        "functions": {
            "betweenness_centrality": {
                "url": "https://www.rustworkx.org/apiref/rustworkx.betweenness_centrality.html#rustworkx.betweenness_centrality",
                "additional_parameters": {
                    "parallel_threshold : int (default=50)": "The number of nodes to calculate the the betweenness centrality in parallel at if the number of nodes in the graph is less than this value it will run in a single thread."
                },
            }
        },
    }
