# https://www.youtube.com/watch?v=aClxtDcdpsQ

def rotate_matrix(matrix, n):
    # should be square matrix
    # take the external layer and rotate each element
    # from one side to the other side. Lyer by Layer rotation

    for layer in xrange(n / 2):
        first = layer
        last = n - layer - 1

        for i in xrange(layer):
            offset = i - first

            # save top
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right - > bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top


def rotate_matrix_minimun():
    original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    reversed_order = original[::-1]
    reversed_order = reversed(original)
    zipped_list = zip(
        reversed_order)  # zip() repeatedly consumes one item from the beginning of each of its arguments and makes a tuple from it, until there are no more items,
    # resulting in [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

    rotated = list(reversed(zip(*original)))



def find_negative_numbers_in_a_ordered_rows_matrix(matrix, n, m):
    """
        https://www.youtube.com/watch?v=5dJSZLmDsxk
                m
          _____________
        | [-3,-2,-1, 1]
      n | [-2, 2, 3, 4] -> 4 negative numbers
        | [4, 5, 7, 8]
    """
    pass