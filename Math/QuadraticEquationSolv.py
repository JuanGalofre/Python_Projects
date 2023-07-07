import math
def cuadratic_solver(a, b, c) -> list:
    solutions = []
    b_squared = b ** 2
    four_a_c = 4 * a * c
    root = math.sqrt((b_squared - four_a_c))
    solutions.append((-b + root) / 2 * a)
    solutions.append((-b - root) / 2 * a)
    return solutions
