import requests
from typing import List
import json


def get_leaderboard(event: str) -> List[str]:
    top_players = []
    r = requests.get("https://api.chess.com/pub/leaderboards/")
    leaderboards = r.json()
    event_leaderboard = leaderboards.get(event, None)
    if not event_leaderboard:
        return []
    for player in event_leaderboard:
        top_players.append(player["username"])
    return top_players
