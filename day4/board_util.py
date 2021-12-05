import numpy as np

def fill(board_array:np.ndarray, num: int, found_array: np.ndarray):
    if num in board_array:
        found_array[np.where(board_array == num)] = 1
    return found_array

def check_complete(array:np.ndarray):
    rows = np.array(array.sum(axis=1))
    cols = np.array(array.sum(axis=0))
    if 5 in rows:
        return True, np.where(rows==5), "row"
    if 5 in cols:
        return True, np.where(cols==5), "col"
    return False, None, None