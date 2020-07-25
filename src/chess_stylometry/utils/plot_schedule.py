from chess_stylometry.utils import time_deltas
import matplotlib.pyplot as plt

player = "PLAYER_NAME"
wdir = "../test"
pgn_name = "games.pgn"
NORMALIZED = True
FILTER_TITLED_ARENAS = True


def get_plot(wdir, player, pgn_name, normalized=NORMALIZED):
    player_dts = time_deltas.get_UTC_dates_and_times(
        wdir, player, pgn_name, filtered=FILTER_TITLED_ARENAS
    )
    hour_to_count = [0 for _ in range(24)]
    for dt in player_dts:
        hour = dt.hour
        hour_to_count[hour] += 1
    if normalized:
        total_games = len(player_dts)
        for idx, count in enumerate(hour_to_count):
            hour_to_count[idx] = int(100 * count / total_games)

    return hour_to_count


if __name__ == "__main__":
    player_hour_to_count = get_plot(wdir, player, pgn_name, normalized=NORMALIZED)
    plt.figure()
    plt.plot(player_hour_to_count)
    if NORMALIZED:
        title = "Percent of games played per hour of the day for {}"
        ylabel = "% of games played"
    else:
        title = "Number of games played per hour of the day for {}"
        ylabel = "# of games played"
    if FILTER_TITLED_ARENAS:
        title = title + " (Excluding Titled Arenas)"
    plt.title(title.format(player))
    plt.xlabel("Hour of the day (UTC)")
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()
