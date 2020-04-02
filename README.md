# Chess Stylometry

The purpose of this project is to build analytical tools that enable the creation and comparison of player-specific sytlometric signatures from an arbitrary set of games.

The inspiration of this project was the bullet chess (1 minute per side) match between current world champion Magnus Carlsen (DrNykerstein) vs. the young prodigy Alireza "The Razor" Firouzja. The match took place on April Fool's Day, sparking wild speculation that the players had switched accounts as a joke. The matter could not be settled, however, until now.

## More details

Main factor:
* Opening choice (with descending weight based on move depth)

Secondary factor:
* Average centipawn loss

## Technical flow

1. User specifies a group of games in PGN format to analyze
2. The program analyzes each game, and creates tables of openings 

