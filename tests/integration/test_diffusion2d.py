"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    w = 20.
    h = 30.
    dx = 0.2
    dy = 0.4
    d = 2.
    T_cold = 200.
    T_hot = 500.
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    assert round(solver.dt, 3) == 0.008


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    w = 3. 
    h = 2.5 
    dx = 1.
    dy = 0.5
    d = 2.
    T_cold = 200.
    T_hot = 500.
    solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)
    solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)
    u = solver.set_initial_condition()
    u_expected = np.array([
            [200., 200., 200., 200., 200.],
            [200., 200., 200., 200., 200.],
            [200., 200., 200., 200., 200.]
        ])
    np.testing.assert_array_equal(u, u_expected, "Expected array:\n{}\nGot:\n{}\n".format(u_expected, u))
