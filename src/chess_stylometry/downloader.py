import requests
import os
from chess_stylometry.cli import Arguments
import lichess.api
from lichess.format import SINGLE_PGN


def make_folder(args: Arguments):
    if not os.path.isdir(args.path_to_pgns):
        os.makedirs(args.path_to_pgns)


def download_chesscom(args: Arguments):
    filename = os.path.join(
        args.path_to_pgns,
        "{}_{}_{}_{}_{}.pgn".format(
            args.player_name,
            args.start_year,
            args.start_month,
            args.end_year,
            args.end_month,
        ),
    )
    print("Writing PGNs to", filename)
    with open(filename, "w+") as f:
        cur_year = args.start_year
        while cur_year <= args.end_year:
            end_month = args.end_month if cur_year == args.end_year else 12
            for month in range(args.start_month, end_month + 1):
                print("Downloading from {}/{}".format(month, cur_year))
                r = requests.get(
                    "https://api.chess.com/pub/player/{}/games/{}/{}/pgn".format(
                        args.player_name, cur_year, month
                    )
                )
                f.write(r.text)
                f.write("\n\n")
            cur_year += 1

        print("Finished.")


def download_lichess(args: Arguments):
    filename = os.path.join(args.path_to_pgns, "games.pgn")
    print("Writing PGNs to", filename)
    with open(filename, "w+") as f:
        games = lichess.api.user_games(args.player_name, format=SINGLE_PGN)
        f.write(games)

    print("Finished.")


def download(args: Arguments):
    make_folder(args)

    if args.pgn_source == "C":
        download_chesscom(args)
    else:
        download_lichess(args)
