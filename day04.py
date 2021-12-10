GRID_SIZE = 5

# Bingo numbers and grids.
def get_b_and_g(lines):
    bingo_numbers = []
    grids = []
    is_first = True
    for line in lines:
        if is_first:
            bingo_numbers = [int(s) for s in line.split(",") if s.isdigit()]
            is_first = False
            continue
        if line == "":
            grids.append([])
        else:
            grids[-1].extend([int(s) for s in line.split(" ") if s.isdigit()])
    return (bingo_numbers, grids)

# (win_order, win_numbers)
def play_data(bingo_numbers, grids):
    grid_win_order = []
    grid_win_numbers = [-1] * len(grids)
    # If a number is 5, It's a win.
    grid_rows = [[0] * GRID_SIZE for grid in grids]
    grid_cols = [[0] * GRID_SIZE for grid in grids]
    # I hate Python.
    # [[0] * 5] * 5 != [[0] * 5 for i in range(5)]

    for number in bingo_numbers:
        for gi, grid in enumerate(grids):
            if grid_win_numbers[gi] != -1:
                continue

            y = -1
            for ci, cell in enumerate(grid):
                if ci % GRID_SIZE == 0:
                    y += 1
                if cell == number:
                    x = ci - y * GRID_SIZE
                    grid_rows[gi][x] += 1
                    grid_cols[gi][y] += 1

                    if grid_rows[gi][x] == GRID_SIZE \
                    or grid_cols[gi][y] == GRID_SIZE:
                        grid_win_numbers[gi] = number
                        grid_win_order.append(gi)
                    break
    return (grid_win_order, grid_win_numbers)

def part1():
    with open("day04.input") as file:
        lines = file.read().split("\n")
        if lines[-1] == "":
            lines.pop()
        bingo_numbers, grids = get_b_and_g(lines)
        grid_win_order, grid_win_numbers = play_data(bingo_numbers, grids)

        # Print the first winner and the score.
        win_number = grid_win_numbers[grid_win_order[0]]
        win_bingo_numbers = bingo_numbers[:bingo_numbers.index(win_number) + 1]
        unmarked_sum = 0
        for cell in grids[grid_win_order[0]]:
            if cell not in win_bingo_numbers:
                unmarked_sum += cell
        score = unmarked_sum * win_number
        print(f"[First board]")
        print(f"Board: {grid_win_order[0] + 1}")
        print(f"Score: {score}")

def part2():
    with open("day04.input") as file:
        lines = file.read().split("\n")
        if lines[-1] == "":
            lines.pop()
        bingo_numbers, grids = get_b_and_g(lines)
        grid_win_order, grid_win_numbers = play_data(bingo_numbers, grids)

        # Print the last winner and the score.
        win_number = grid_win_numbers[grid_win_order[-1]]
        win_bingo_numbers = bingo_numbers[:bingo_numbers.index(win_number) + 1]
        unmarked_sum = 0
        for cell in grids[grid_win_order[-1]]:
            if cell not in win_bingo_numbers:
                unmarked_sum += cell
        score = unmarked_sum * win_number
        print(f"[Last board]")
        print(f"Board: {grid_win_order[-1] + 1}")
        print(f"Score: {score}")

part1()
part2()
