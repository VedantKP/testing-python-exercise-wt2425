"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np

def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20.,h=30.,dx=0.2,dy=0.4)

    # Check that nx and nx are correctly computed based on w, dx and h, dy resp.
    assert solver.nx == 100
    assert solver.ny == 75


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.dx = 0.2
    solver.dy = 0.4
    solver.initialize_physical_parameters(d=2.,T_cold=200.,T_hot=500.)
    
    # Check that value of dt is correctly computed based on input settings
    assert round(solver.dt, 3) == 0.008


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.nx = 100
    solver.ny = 150
    solver.T_cold = 100.
    solver.dx = 0.2
    solver.dy = 0.2
    solver.T_hot = 400.
    u = solver.set_initial_condition()

    # Check shape is appropriate
    assert u.shape[0] == solver.nx
    assert u.shape[1] == solver.ny 

    # Check that corners are cold
    assert u[0, 0] == solver.T_cold
    assert u[0, -1] == solver.T_cold
    assert u[-1, 0] == solver.T_cold
    assert u[-1, -1] == solver.T_cold

    # checking that values in the circle center are hot cannot be tested as it depends on the values 
    # of r, cx, cy. These values are not parameters of the class and hardcoding them here would bind
    # the test to the settings of the actual function thus losing generality. This would have been
    # testable if there was a choice to set these values by the user.