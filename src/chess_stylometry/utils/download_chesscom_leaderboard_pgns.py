from chess_stylometry import downloader
from chess_stylometry.utils import get_chesscom_leaderboard
from chess_stylometry.cli import Arguments


if __name__ == "__main__":
    leaderboard = get_chesscom_leaderboard.get_leaderboard("live_blitz")
    for player in leaderboard:
        args = Arguments(path_to_pgns=f"../test/{player}/", analyze=False, download=True, player_name=player, pgn_source="C",
                         start_year=2018, end_year=2020, start_month=1, end_month=12)
        downloader.make_folder(args)
        downloader.download_chesscom(args)


