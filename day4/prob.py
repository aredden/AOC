import dill as pkl
import numpy as np

data = pkl.load(open("day4_input.pkl", "rb"))
toprow = data["toprow"]
grid = data["grid"]
empty = np.zeros_like(grid)


def fill(board_array: np.ndarray, num: int, found_array: np.ndarray):
    if num in board_array:
        found_array[np.where(board_array == num)] = 1
    return found_array


def check_complete(array: np.ndarray):
    rows = np.array(array.sum(axis=1))
    cols = np.array(array.sum(axis=0))
    if 5 in rows:
        return True, np.where(rows == 5), "row"
    if 5 in cols:
        return True, np.where(cols == 5), "col"
    return False, None, None


def fill_all(num: int, grid: np.ndarray, empty: np.ndarray):
    rem_indexes = []
    for i, board in enumerate(grid):
        empty[i] = fill(board, num, empty[i])
        complete, index, wintype = check_complete(empty[i])
        if complete:
            rem_indexes.append(i)
            if len(grid) - len(rem_indexes) < 1:
                print(
                    f"Found winner! Board at index {i}, "
                    + f"Win type: {wintype}, board: \n{board}, \n"
                    + f"Winning index: {index}, winning number: {num}\n"
                    + f"Filled locations: \n{empty[i]}"
                )
                brd: np.ndarray = board[:].flatten()
                brd[np.where(empty[i, :].flatten() == 1)] = 0
                print(f"total iteration: {total_count}")
                print(f"total sum: {np.sum(brd)}")
                print(f"Winning amount: {np.sum(brd)*num}\n")
                exit()
    grid = np.delete(grid, rem_indexes, 0)
    empty = np.delete(empty, rem_indexes, 0)
    return grid, empty


total_count = 0
for num in toprow:
    total_count += 1
    grid, empty = fill_all(num, grid, empty)
