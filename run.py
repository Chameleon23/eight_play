from helper_functions import *


def solve(current_state, smart_search=False):
    # how many step need algorithm to solve problem
    count_step = 0

    queue = [current_state]

    # add start matrix in "discovered matrix"
    discovered_matrix.add(current_state.tobytes())

    while queue:
        count_step += 1
        print(f"step: {count_step}")
        current_state = queue.pop(0)

        # if target is final matrix, problem solved, return path
        if np.array_equal(current_state, final_state):
            return reconstruct_solution_path(init_array, current_state, path_map)

        # find hole
        row, column = get_hole_coordinate_row_column(current_state)

        # move up
        if row - 1 >= 0:
            new_state = swap(current_state, row, column, row - 1, column)
            manage_queue_and_path(queue, current_state, new_state, discovered_matrix, path_map, smart_search)

        # move left
        if column - 1 >= 0:
            new_state = swap(current_state, row, column, row, column - 1)
            manage_queue_and_path(queue, current_state, new_state, discovered_matrix, path_map, smart_search)

        # move down
        if row + 1 <= 2:
            new_state = swap(current_state, row, column, row + 1, column)
            manage_queue_and_path(queue, current_state, new_state, discovered_matrix, path_map, smart_search)

        # move right
        if column + 1 <= 2:
            new_state = swap(current_state, row, column, row, column + 1)
            manage_queue_and_path(queue, current_state, new_state, discovered_matrix, path_map, smart_search)


# set for already discovered nodes
discovered_matrix = set()

# map child_matrix -> parent_matrix
path_map = {}


# final solution (target)
final_state = np.array([
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
])

# starting matrix
init_array = np.array([
    [6, 8, 3],
    [5, 9, 7],
    [4, 1, 2]
])


path = solve(init_array, smart_search=False)

print_path(path)
