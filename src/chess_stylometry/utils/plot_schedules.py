from chess_stylometry.utils import time_deltas
import matplotlib.pyplot as plt
import datetime

player1 = "konevlad"
player2 = "DrNykterstein"
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
    player1_hour_to_count = get_plot(wdir, player1, pgn_name)
    player2_hour_to_count = get_plot(wdir, player2, pgn_name)
    plt.figure()
    plt.subplot(211)
    plt.plot(player1_hour_to_count)
    plt.title(f"Number of games played per hour of the day for {player1}")
    plt.xlabel("Hour of the day (UTC)")
    plt.ylabel("# of games played")
    plt.subplot(212)
    plt.plot(player2_hour_to_count)
    plt.title(f"Number of games played per hour of the day for {player2}")
    plt.xlabel("Hour of the day (UTC)")
    plt.ylabel("# of games played")
    plt.tight_layout()
    plt.show()
