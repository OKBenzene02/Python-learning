import math
import heapq

ROW = 9
COL = 10

def is_valid(row, col):
    return 0 <= row < ROW and 0 <= col < COL

def is_unblocked(grid, row, col):
    return grid[row][col] == 1

def is_destination(row, col, dest):
    return (row, col) == dest

def calculate_h_value(row, col, dest):
    return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2)

def trace_path(cell_details, dest):
    print("The Path is ", end="")
    row, col = dest
    path = []

    while not (cell_details[row][col]['parent_i'] == row and cell_details[row][col]['parent_j'] == col):
        path.append((row, col))
        temp_row, temp_col = cell_details[row][col]['parent_i'], cell_details[row][col]['parent_j']
        row, col = temp_row, temp_col

    path.append((row, col))
    path.reverse()

    for p in path:
        print(f"-> {p}", end=" ")
    print()

def a_star_search(grid, src, dest):
    if not is_valid(*src) or not is_valid(*dest):
        print("Source or destination is invalid")
        return

    if not is_unblocked(grid, *src) or not is_unblocked(grid, *dest):
        print("Source or destination is blocked")
        return

    if is_destination(*src, dest):
        print("We are already at the destination")
        return

    closed_list = [[False] * COL for _ in range(ROW)]
    cell_details = [[{'f': math.inf, 'g': math.inf, 'h': math.inf, 'parent_i': -1, 'parent_j': -1} for _ in range(COL)] for _ in range(ROW)]

    src_i, src_j = src
    cell_details[src_i][src_j] = {'f': 0.0, 'g': 0.0, 'h': 0.0, 'parent_i': src_i, 'parent_j': src_j}

    open_list = [(0.0, src_i, src_j)]
    heapq.heapify(open_list)

    found_dest = False

    while open_list:
        f, i, j = heapq.heappop(open_list)
        closed_list[i][j] = True

        successors = [
            (-1, 0), (1, 0), (0, 1), (0, -1),
            (-1, 1), (-1, -1), (1, 1), (1, -1)
        ]

        for di, dj in successors:
            new_i, new_j = i + di, j + dj

            if is_valid(new_i, new_j):
                if is_destination(new_i, new_j, dest):
                    cell_details[new_i][new_j]['parent_i'] = i
                    cell_details[new_i][new_j]['parent_j'] = j
                    print("The destination cell is found")
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                elif not closed_list[new_i][new_j] and is_unblocked(grid, new_i, new_j):
                    g_new = cell_details[i][j]['g'] + (1.0 if di == 0 or dj == 0 else 1.414)
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    if cell_details[new_i][new_j]['f'] == math.inf or cell_details[new_i][new_j]['f'] > f_new:
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        cell_details[new_i][new_j] = {'f': f_new, 'g': g_new, 'h': h_new, 'parent_i': i, 'parent_j': j}

    if not found_dest:
        print("Failed to find the Destination Cell")

# Driver program to test above function
if __name__ == "__main__":
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    src = (8, 0)
    dest = (0, 0)

    a_star_search(grid, src, dest)
