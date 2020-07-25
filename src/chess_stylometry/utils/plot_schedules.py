from chess_stylometry.utils import time_deltas
from chess_stylometry.utils import plot_schedule
import matplotlib.pyplot as plt
import datetime

player1 = "konevlad"
player2 = "DrNykterstein"
wdir = "../test"
pgn_name = "games.pgn"
NORMALIZED = True
FILTER_TITLED_ARENAS = True


if __name__ == "__main__":
    title = "Number of games played per hour of the day for {}"
    if FILTER_TITLED_ARENAS:
        title = title + " (Excluding Titled Arenas)"
    player1_hour_to_count = plot_schedule.get_plot(
        wdir, player1, pgn_name, normalized=NORMALIZED
    )
    player2_hour_to_count = plot_schedule.get_plot(
        wdir, player2, pgn_name, normalized=NORMALIZED
    )
    plt.figure()
    plt.subplot(211)
    plt.plot(player1_hour_to_count)
    plt.title(title.format(player1))
    plt.xlabel("Hour of the day (UTC)")
    plt.ylabel("# of games played")
    plt.subplot(212)
    plt.plot(player2_hour_to_count)
    plt.title(title.format(player2))
    plt.xlabel("Hour of the day (UTC)")
    plt.ylabel("# of games played")
    plt.tight_layout()
    plt.show()
