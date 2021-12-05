from aocd import get_data
import dill as pkl
import numpy as np


itext = get_data()
lines = itext.splitlines(keepends=False)

# Build input array.
toprow = [int(i.strip()) for i in lines.pop(0).split(",")]

print(toprow[0:10])

# Split by each board (each board is separated via two newlines)
boards = itext.split("\n" * 2)
boards.pop(0)

# Create array of boards.
grid = list()
for line in boards:
    curlist = list()
    for item in line.split("\n"):
        curlist.append([int(x.strip()) for x in item.split()])
    grid.append(curlist)
for g in grid:
    assert len(g) == 5, f"The grid is not the correct size: {len(g)} not 5"
    for gi in g:
        assert len(gi) == 5, f"The grid row is not the correct size: {len(gi)} not 5"

# Convert to numpy arrays
grid = np.array(grid, dtype=np.int32)
toprow = np.array(toprow, dtype=np.int32)

pkl.dump({"toprow": toprow, "grid": grid}, open("day4_input.pkl", "wb"))
