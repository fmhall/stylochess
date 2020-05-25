#! /usr/bin/env python3
import chess_graph

player1 = "konevlad"
player2 = "DrNykterstein"
wdir = "../test"
pgn_name = "games.pgn"

filename = "/".join([wdir, player2, pgn_name])

chess_graph.graph(
    filename,
    depth=5,
    shade=True,
    fragmentation_percentage=.01,
    should_defragment=True,
    custom_branching=False,
    should_download=False,
    download_format="png",
    download_name="fig1",
)
