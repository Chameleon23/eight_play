import numpy as np


def print_table(array):
    print('*' * 9)

    for each_row in array:
        print('*', end=' ')
        for element in each_row:
            print(element, end=' ')
        print('*')

    print('*' * 9)


def get_hole_coordinate_row_column(array):

    finded_number = array.argmax()
    column_index = finded_number % 3
    row_index = finded_number // 3

    return row_index, column_index


# move number to free space
def swap(array, row, column, new_row, new_column):
    array = array.copy()
    array[row][column], array[new_row][new_column] = array[new_row][new_column], array[row][column]
    return array


def manage_queue_and_path(queue, current_state, new_state, discovered_matrix, path_map, smart_search):
    # we can't save matrix in hash map so we must convert it in to bytes
    new_matrix_in_bytes = new_state.tobytes()

    if smart_search:
        # if we never met this matrix already
        if new_matrix_in_bytes not in discovered_matrix:

            # mark matrix as discovered
            discovered_matrix.add(new_matrix_in_bytes)

            queue.append(new_state)

            # save parent of current matrix
            path_map[new_matrix_in_bytes] = current_state.tobytes()
    else:
        queue.append(new_state)
        path_map[new_matrix_in_bytes] = current_state.tobytes()


# we saved bytes in hash map so it's time to convert it in matrix again
def reconstruct_array_from_bytes(array):
    array = np.frombuffer(array, dtype=int)
    array = array.reshape((3, 3))
    return array


def reconstruct_solution_path(init_array, solution_array, path_map):

    current_array_in_bytes = solution_array.tobytes()
    init_array_in_bytes = init_array.tobytes()

    # variable for reconstructed path
    solution_path = [current_array_in_bytes]

    # until
    while current_array_in_bytes != init_array_in_bytes:
        # find and append current matrix parent in path variable
        current_array_in_bytes = path_map[current_array_in_bytes]
        solution_path.append(current_array_in_bytes)

    # we have list child to parent order, but we need opposite parent to child
    # as we know init matrix is root (parent)
    solution_path.reverse()

    # convert bytes in to matrix (in hash map we have bytes)
    solution_path = [reconstruct_array_from_bytes(each) for each in solution_path]

    return solution_path


def print_path(path):
    for move_step, each_node in enumerate(path):
        print(move_step + 1)
        print_table(each_node)
