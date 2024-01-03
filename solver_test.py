import solver


NUM = """
3
7 4
2 4 6
8 5 9 3
"""


def is_solved():
    assert solver.solver()


def test_solver():
    assert solver.solver(NUM) == 23
