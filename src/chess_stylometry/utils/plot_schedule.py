from chess_stylometry.utils import time_deltas
import matplotlib.pyplot as plt

player = "PLAYER_NAME"
wdir = "../test"
pgn_name = "games.pgn"


def get_plot(wdir, player, pgn_name):
    player_dts = time_deltas.get_UTC_dates_and_times(wdir, player, pgn_name)
    hour_to_count = [0 for _ in range(24)]
    for dt in player_dts:
        hour = dt.hour
        hour_to_count[hour] += 1
    return hour_to_count


if __name__ == "__main__":
    player_hour_to_count = get_plot(wdir, player, pgn_name)
    plt.figure()
    plt.plot(player_hour_to_count)
    plt.title(f"Number of games played per hour of the day for {player}")
    plt.xlabel("Hour of the day (UTC)")
    plt.ylabel("# of games played")
    plt.tight_layout()
    plt.show()
