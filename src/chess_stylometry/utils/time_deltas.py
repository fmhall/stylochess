import chess.pgn
from datetime import datetime
from datetime import timedelta
from typing import NamedTuple, List

player1 = "konevlad"
player2 = "DrNykterstein"
wdir = "../test"
pgn_name = "games.pgn"


def get_UTC_dates_and_times(wdir, player, pgn_name):
    filename = "/".join([wdir, player, pgn_name])
    print(filename)
    pgn = open(filename)
    utc_timestamps = []
    while True:
        offset = pgn.tell()
        headers = chess.pgn.read_headers(pgn)
        if not headers:
            break
        utc_date = headers["UTCDate"]
        utc_time = headers["UTCTime"]
        tstamp = utc_date.replace(".", "-") + "T" + utc_time
        dt = datetime.fromisoformat(tstamp)
        utc_timestamps.append(dt)
    return sorted(utc_timestamps)


class DeltaInfo(NamedTuple):
    player1: str
    player1_dt: datetime
    player2: str
    player2_dt: datetime
    delta: timedelta


def compare_dt_lists(
    player1_dts, player2_dts, player1, player2
) -> [DeltaInfo, List[DeltaInfo]]:
    a1, a2 = iter(player1_dts), iter(player2_dts)
    i1, i2 = next(a1), next(a2)
    min_dif = abs(i1 - i2)
    z_difs = []
    print(i1 > i2)
    print(min_dif)
    i1, i2 = next(a1), next(a2)
    print(i1 > i2)
    print(min_dif)
    min_info = None
    difs = []
    while True:
        dif = abs(i1 - i2)
        d_info = DeltaInfo(player1, i1, player2, i2, dif)
        difs.append(d_info)
        if dif < min_dif:
            min_dif = dif
            min_info = d_info
            if min_dif == timedelta():
                z_difs.append(min_info)
        if i1 > i2:
            try:
                i2 = next(a2)
            except StopIteration:
                break
        else:
            try:
                i1 = next(a1)
            except StopIteration:
                break
    return min_info, difs


if __name__ == "__main__":
    player1_dts = get_UTC_dates_and_times(wdir, player1, pgn_name)
    player2_dts = get_UTC_dates_and_times(wdir, player2, pgn_name)
    min_info, difs = compare_dt_lists(player1_dts, player2_dts, player1, player2)
    print(min_info)
    difs.sort(key=lambda x: x.delta)
    for dif in difs[:10]:
        print(dif.delta)
        print(dif.player1)
        print(dif.player2)
        print(dif.player1_dt)
