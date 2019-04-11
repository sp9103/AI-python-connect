def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        return ArithmeticError
    return [sum(element) for element in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [element[0] * 2 - sum(element) for element in zip(*vector_variables)]


def scalar_vector_product(alpha, vector_variable):
    return [alpha * element for element in vector_variable]


def matrix_size_check(*matrix_variables):
    return all([len(matrix_variables[0]) == len(matrix) and len(row) == len(matrix_variables[0][i]) for matrix in matrix_variables[1:] for i, row in enumerate(matrix)])


def is_matrix_equal(*matrix_variables):
    return all([len(matrix_variables[0]) == len(matrix) and len(row) == len(matrix_variables[0][i]) and matrix_variables[0][i][j] == element
                for matrix in matrix_variables[1:] for i, row in enumerate(matrix) for j, element in enumerate(row)])


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[sum(element) for element in zip(*rows)] for rows in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[2 * matrix_variables[0][i][j] - sum(element) for j, element in enumerate(zip(*rows))] for i, rows in enumerate(zip(*matrix_variables))]


def matrix_transpose(matrix_variable):
    return list(zip(*matrix_variable))


def scalar_matrix_product(alpha, matrix_variable):
    return [[ alpha * element for element in row ] for row in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):
    return len(matrix_a[0]) == len(matrix_transpose(matrix_b)[0])


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return [ [ [sum(t[0] * t[1]  for t in zip(row_a, row_b))] for row_b in matrix_transpose(matrix_b)] for row_a in matrix_a]
