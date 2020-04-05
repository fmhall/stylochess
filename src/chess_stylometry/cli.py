import os
import argparse
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

abs_path = os.path.dirname(os.path.abspath(__file__))


@dataclass
class Arguments:
    path_to_pgns: str
    analyze: bool
    download: bool
    player_name: Optional[str]
    pgn_source: Optional[str]
    start_month: Optional[int]
    end_month: Optional[int]
    start_year: Optional[int]
    end_year: Optional[int]


def get_opts() -> argparse.Namespace:

    arg_parser = argparse.ArgumentParser(
        description="Command line interface for the chess stylometry.",
        usage="stylochess --help",
    )
    arg_parser.add_argument(
        "--path-to-pgns",
        help="Path to a folder of pgn files or a single pgn file",
        type=str,
    )
    arg_parser.add_argument(
        "--analyze", help="Boolean flag to analyze", type=bool, default=False
    )
    arg_parser.add_argument(
        "--download", help="Boolean flag to download PGNS", type=bool, default=False
    )
    arg_parser.add_argument(
        "--player-name",
        help="Account name of person you would like to download PGNS from",
        type=str,
        default=None,
    )
    arg_parser.add_argument(
        "--pgn-source",
        help="Lichess (L) or Chess.com (C). Default lichess",
        choices={"L", "C"},
        default="L",
    )
    arg_parser.add_argument(
        "--start-month",
        help="Starting month of PGNs to download (1-12)",
        type=int,
        default=1,
    )
    arg_parser.add_argument(
        "--end-month",
        help="Ending month of PGNs to download (1-12)",
        type=int,
        default=12,
    )
    arg_parser.add_argument(
        "--start-year",
        help="Starting year of PGNs to download (2012-)",
        type=int,
        default=None,
    )
    arg_parser.add_argument(
        "--end-year",
        help="Ending month of PGNs to download (2012-)",
        type=int,
        default=None,
    )
    opts, _unknown = arg_parser.parse_known_args()
    return opts


def type_arguments(opts: argparse.Namespace) -> Arguments:
    if opts.download:
        assert all(
            [
                opts.player_name,
                opts.start_month,
                opts.end_month,
                opts.start_year,
                opts.end_year,
            ]
        )

    return Arguments(
        path_to_pgns=opts.path_to_pgns,
        analyze=opts.analyze,
        download=opts.download,
        player_name=opts.player_name,
        pgn_source=opts.pgn_source,
        start_month=opts.start_month,
        end_month=opts.end_month,
        start_year=opts.start_year,
        end_year=opts.end_year,
    )


def parse_arguments(args: Arguments):
    if args.download:
        cur_year = datetime.today().year
        assert 1 <= args.start_month <= 12
        assert 1 <= args.end_month <= 12
        assert 2012 <= args.start_year <= cur_year
        assert args.start_year <= args.end_year <= cur_year
        assert args.player_name.isalnum()


def print_arguments(args: Arguments):
    print(args)
