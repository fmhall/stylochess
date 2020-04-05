import requests
import os
from chess_stylometry.cli import Arguments


def make_folder(args: Arguments):
    abs_path = os.path.dirname(os.path.abspath(__file__))
    folder_path = args.path_to_pgns
    if not os.path.isabs(folder_path):
        print("creating absolute", abs_path, folder_path)
        folder_path = os.path.join(abs_path, folder_path)
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    print("Writing PGNs to", folder_path)
    return folder_path


def download_chesscom(args: Arguments, abs_folder_path: str):
    filename = os.path.join(
        abs_folder_path,
        "{}_{}_{}_{}_{}.pgn".format(
            args.player_name,
            args.start_year,
            args.start_month,
            args.end_year,
            args.end_month,
        ),
    )
    print(filename)
    with open(filename, "w+") as f:
        cur_year = args.start_year
        while cur_year <= args.end_year:
            end_month = args.end_month if cur_year == args.end_year else 12
            for month in range(args.start_month, end_month + 1):
                print("Downloading from {}/{}".format(month, args.start_year))
                r = requests.get(
                    "https://api.chess.com/pub/player/{}/games/{}/{}/pgn".format(
                        args.player_name, args.start_year, month
                    )
                )
                f.write(r.text)
            cur_year += 1
        print("Wrote PGNs to", filename)
        print("Wrote PGNs to", args.path_to_pgns)
        print("Finished.")


def download_lichess(args: Arguments, abs_folder_path: str):
    print("Lichess download")
    pass


def download(args: Arguments):
    abs_path_to_folder = make_folder(args)
    if args.pgn_source == "C":
        download_chesscom(args, abs_path_to_folder)
    else:
        download_lichess(args, abs_path_to_folder)
