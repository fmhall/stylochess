import requests
import os

def download():
    PLAYER = "IMRosen"
    STARTING_YEAR = 2015
    CURRENT_YEAR = 2020
    BASE_PATH = "/Users/masonhall/personal/pgns"
    folder_path = "{}/{}".format(BASE_PATH, PLAYER)
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    print("Writing PGNs to", folder_path)
    while STARTING_YEAR <= CURRENT_YEAR:
        filename = folder_path + "/{}.pgn".format(STARTING_YEAR)
        with open(filename, "w") as f:
            for month in range(1, 13):
                print("Downloading from {}/{}".format(month, STARTING_YEAR))
                r = requests.get(
                    "https://api.chess.com/pub/player/{}/games/{}/{}/pgn".format(
                        PLAYER, STARTING_YEAR, month
                    )
                )
                f.write(r.text)
            STARTING_YEAR += 1
        print("Wrote PGNs to", filename)
    print("Wrote PGNs to", folder_path)
    print("Finished.")
