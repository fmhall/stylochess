from typing import NamedTuple

ECO_dict = {}


class Opening(NamedTuple):
    ECO: str
    name: str
    fen: str


with open("ECOs.txt", "r") as f:
    for line in f.readlines():
        if "FullOpening" in line:
            idx = line.find("FullOpening")
            start = idx + 12
            useful = line[start:]
            parts = useful.split(",")
            if len(parts) >= 3:
                eco = parts[0]
                name = parts[1]
                fen = parts[2].strip(")")
                ECO_dict[fen] = Opening(ECO=eco, name=name, fen=fen)
print(ECO_dict)
