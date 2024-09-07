# POC for rustworkx-backend

Simple POC for implementing a [rustworkx](https://www.rustworkx.org/index.html) backend for [networkx](https://networkx.org/documentation/stable/index.html).

## Testing

```bash
pytest --pyargs networkx.algorithms.centrality.tests -k TestBetweennessCentrality
```

## License

This repo is under the [MIT License](LICENSE).
