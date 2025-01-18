"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import unittest

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()


    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w=20.,h=30.,dx=0.2,dy=0.4)

        # Check that nx and nx are correctly computed based on w, dx and h, dy resp.
        self.assertEqual(self.solver.nx, 100)
        self.assertEqual(self.solver.ny, 75)


    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.dx = 0.2
        self.solver.dy = 0.4
        self.solver.initialize_physical_parameters(d=2.,T_cold=200.,T_hot=500.)
        
        # Check that value of dt is correctly computed based on input settings
        self.assertAlmostEqual(self.solver.dt, 0.008)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.nx = 100
        self.solver.ny = 150
        self.solver.T_cold = 100.
        self.solver.dx = 0.2
        self.solver.dy = 0.2
        self.solver.T_hot = 400.
        u = self.solver.set_initial_condition()
        
        # Check shape is appropriate
        self.assertEqual(u.shape, (self.solver.nx, self.solver.ny))

        # Check that corners are cold
        self.assertEqual(u[0, 0], self.solver.T_cold)
        self.assertEqual(u[0, -1], self.solver.T_cold)
        self.assertEqual(u[-1, 0], self.solver.T_cold)
        self.assertEqual(u[-1, -1], self.solver.T_cold)

        # checking that values in the circle center are hot cannot be tested as it depends on the values 
        # of r, cx, cy. These values are not parameters of the class and hardcoding them here would bind
        # the test to the settings of the actual function thus losing generality. This would have been
        # testable if there was a choice to set these values by the user.