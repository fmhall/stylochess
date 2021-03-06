from chess_stylometry import cli
from chess_stylometry import downloader
from chess_stylometry import analyzer

if __name__ == "__main__":
    opts = cli.get_opts()
    args = cli.type_arguments(opts)
    cli.parse_arguments(args)

    if args.download:
        # Download PGNS
        downloader.download(args)
        pass
    if args.analyze:
        # Analyze
        # analyzer.analyze(args)
        pass
