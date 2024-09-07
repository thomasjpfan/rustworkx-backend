from inspect import signature
from functools import wraps


def _convert_dict_to_values(rx_graph, output_dict):
    node_names = rx_graph.nodes()
    return {node_names[k]: v for k, v in output_dict.items()}


def _filter_expected_values(func, nx_func, converter=None):
    supported_params = set(signature(func).parameters)
    orig_params = signature(nx_func).parameters

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_as_kwargs = dict(zip(orig_params, args))

        # Raise `NotImplementedError` for unsupported parameters
        filter_kwargs = {**kwargs}
        graph = args_as_kwargs["G"]
        del args_as_kwargs["G"]

        for key, value in args_as_kwargs.items():
            if key in supported_params:
                filter_kwargs[key] = value
            elif value is not None and key != "seed":
                raise NotImplementedError(f"{key} parameter is not supported")

        from ._interface import RustworkXGraph

        if isinstance(graph, RustworkXGraph):
            graph = graph.graph_object

        out = func(graph, **filter_kwargs)
        if converter is None:
            return out
        return converter(graph, out)

    return wrapper
