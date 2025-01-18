# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

I am working on a Windows machine, so initially pytest was not able to detect the class correctly and giving the following output:

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> pytest .\tests\unit\test_diffusion2d_functions.py
======================================================================== test session starts ========================================================================
platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425
collected 0 items / 1 error

============================================================================== ERRORS =============================================================================== 
_____________________________________________________ ERROR collecting tests/unit/test_diffusion2d_functions.py _____________________________________________________ 
ImportError while importing test module 'C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Program Files\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests\unit\test_diffusion2d_functions.py:5: in <module>
    from diffusion2d import SolveDiffusion2D
E   ModuleNotFoundError: No module named 'diffusion2d'
====================================================================== short test summary info ====================================================================== 
ERROR tests/unit/test_diffusion2d_functions.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
========================================================================= 1 error in 0.16s ==========================================================================
```

**Solution**: Introduced `__init__.py` files in all directories and ran pytest as a module using: `python -m pytest`


#### Changing `self.nx = int(w / dx)` to `self.nx = int(h / dx)` in initialize_domain

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m pytest .\tests\unit\test_diffusion2d_functions.py
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425
collected 3 items

tests\unit\test_diffusion2d_functions.py F..                                                                                                                     [100%]

============================================================================== FAILURES ===============================================================================
_______________________________________________________________________ test_initialize_domain ________________________________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20.,h=30.,dx=0.2,dy=0.2)
    
>       assert solver.nx == 100
E       assert 150 == 100
E        +  where 150 = <diffusion2d.SolveDiffusion2D object at 0x000001C3891FA9C0>.nx

tests\unit\test_diffusion2d_functions.py:15: AssertionError
========================================================================== warnings summary =========================================================================== 
..\..\..\..\..\..\..\..\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37
  C:\Users\Vedant\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37: DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
    EPOCH = datetime.datetime.utcfromtimestamp(0)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================= short test summary info ======================================================================= 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 150 == 100
=============================================================== 1 failed, 2 passed, 1 warning in 0.94s ================================================================ 
```


#### Changing to `dx2, dy2 = self.dx * self.dy, self.dx * self.dy` in initialize_physical_parameters 

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m pytest .\tests\unit\test_diffusion2d_functions.py
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425
collected 3 items

tests\unit\test_diffusion2d_functions.py .F.                                                                                                                     [100%]

============================================================================== FAILURES ===============================================================================
_________________________________________________________________ test_initialize_physical_parameters _________________________________________________________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = 0.2
        solver.dy = 0.4
        solver.initialize_physical_parameters(d=2.,T_cold=200.,T_hot=500.)
>       assert round(solver.dt, 3) == 0.008
E       assert 0.01 == 0.008
E        +  where 0.01 = round(0.010000000000000002, 3)
E        +    where 0.010000000000000002 = <diffusion2d.SolveDiffusion2D object at 0x000001B8AEEAC110>.dt

tests\unit\test_diffusion2d_functions.py:27: AssertionError
------------------------------------------------------------------------ Captured stdout call -------------------------------------------------------------------------
dt = 0.010000000000000002
========================================================================== warnings summary ===========================================================================
..\..\..\..\..\..\..\..\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37
  C:\Users\Vedant\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37: DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
    EPOCH = datetime.datetime.utcfromtimestamp(0)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================= short test summary info ======================================================================= 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.01 == 0.008
=============================================================== 1 failed, 2 passed, 1 warning in 0.97s ================================================================ 
```

#### Changing to `u = self.T_hot * np.ones((self.nx, self.ny))` in set_initial_condition 

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m pytest .\tests\unit\test_diffusion2d_functions.py
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425
collected 3 items

tests\unit\test_diffusion2d_functions.py ..F                                                                                                                     [100%]

============================================================================== FAILURES ===============================================================================
_____________________________________________________________________ test_set_initial_condition ______________________________________________________________________

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

        assert u.shape[0] == solver.nx # 100
        assert u.shape[1] == solver.ny # 150

>       assert u[0, 0] == solver.T_cold
E       assert 400.0 == 100.0
E        +  where 100.0 = <diffusion2d.SolveDiffusion2D object at 0x000001AD4473EAE0>.T_cold

tests\unit\test_diffusion2d_functions.py:46: AssertionError
========================================================================== warnings summary =========================================================================== 
..\..\..\..\..\..\..\..\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37
  C:\Users\Vedant\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37: DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
    EPOCH = datetime.datetime.utcfromtimestamp(0)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================= short test summary info ======================================================================= 
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert 400.0 == 100.0
=============================================================== 1 failed, 2 passed, 1 warning in 0.90s ================================================================ 
```

### unittest log

#### Changing `self.nx = int(w / dx)` to `self.nx = int(h / dx)` in initialize_domain

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m unittest .\tests\unit\test_diffusion2d_functions.py
Fdt = 0.008000000000000002
..
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_domain)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 21, in test_initialize_domain
    self.assertEqual(self.solver.nx, 100)
AssertionError: 150 != 100

----------------------------------------------------------------------
Ran 3 tests in 0.006s

FAILED (failures=1)
```

#### Changing to `dx2, dy2 = self.dx * self.dy, self.dx * self.dy` in initialize_physical_parameters

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m unittest .\tests\unit\test_diffusion2d_functions.py
.dt = 0.010000000000000002
F.
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_physical_parameters)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 34, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, 0.008)
AssertionError: 0.010000000000000002 != 0.008 within 7 places (0.0020000000000000018 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.006s

FAILED (failures=1)
```

#### Changing to `u = self.T_hot * np.ones((self.nx, self.ny))` in set_initial_condition

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m unittest .\tests\unit\test_diffusion2d_functions.py
.dt = 0.008000000000000002
.F
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_set_initial_condition)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 52, in test_set_initial_condition
    self.assertEqual(u[0, 0], self.solver.T_cold)
AssertionError: 400.0 != 100.0

----------------------------------------------------------------------
Ran 3 tests in 0.005s

FAILED (failures=1)
```

### Integration test log

#### Changing `self.nx = int(w / dx)` to `self.nx = int(h / dx)` in initialize_domain

This only affects the second test as the first one is independent of the values of nx and ny.

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m pytest .\tests\integration\test_diffusion2d.py
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425
collected 2 items

tests\integration\test_diffusion2d.py .F                                                                                                                         [100%]

============================================================================== FAILURES ===============================================================================
_____________________________________________________________________ test_set_initial_condition ______________________________________________________________________

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
>       np.testing.assert_array_equal(u, u_expected, "Expected array:\n{}\nGot:\n{}\n".format(u_expected, u))

tests\integration\test_diffusion2d.py:45: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

args = (<built-in function eq>, array([[200., 200., 200., 200., 200.],
       [200., 200., 200., 200., 200.]]), array([[200., 200., 200., 200., 200.],
       [200., 200., 200., 200., 200.],
       [200., 200., 200., 200., 200.]]))
kwds = {'err_msg': 'Expected array:\n[[200. 200. 200. 200. 200.]\n [200. 200. 200. 200. 200.]\n [200. 200. 200. 200. 200.]]\n.... 200. 200. 200.]\n [200. 200. 200. 200. 200.]]\n', 'header': 'Arrays are not equal', 'strict': False, 'verbose': True}

    @wraps(func)
    def inner(*args, **kwds):
        with self._recreate_cm():
>           return func(*args, **kwds)
E           AssertionError: 
E           Arrays are not equal
E           Expected array:
E           [[200. 200. 200. 200. 200.]
E            [200. 200. 200. 200. 200.]
E            [200. 200. 200. 200. 200.]]
E           Got:
E           [[200. 200. 200. 200. 200.]
E            [200. 200. 200. 200. 200.]]
E
E           (shapes (2, 5), (3, 5) mismatch)
E            x: array([[200., 200., 200., 200., 200.],
E                  [200., 200., 200., 200., 200.]])
E            y: array([[200., 200., 200., 200., 200.],
E                  [200., 200., 200., 200., 200.],
E                  [200., 200., 200., 200., 200.]])

C:\Program Files\Python312\Lib\contextlib.py:81: AssertionError
------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------- 
dt = 0.05
========================================================================== warnings summary =========================================================================== 
..\..\..\..\..\..\..\..\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37
  C:\Users\Vedant\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37: DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
    EPOCH = datetime.datetime.utcfromtimestamp(0)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================= short test summary info ======================================================================= 
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError:
=============================================================== 1 failed, 1 passed, 1 warning in 1.11s ================================================================ 
```

#### Changing to `dx2, dy2 = self.dx * self.dy, self.dx * self.dy` in initialize_physical_parameters

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m pytest .\tests\integration\test_diffusion2d.py
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425
collected 2 items

tests\integration\test_diffusion2d.py F.                                                                                                                         [100%]

============================================================================== FAILURES ===============================================================================
_________________________________________________________________ test_initialize_physical_parameters _________________________________________________________________

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
>       assert round(solver.dt, 3) == 0.008
E       assert 0.01 == 0.008
E        +  where 0.01 = round(0.010000000000000002, 3)
E        +    where 0.010000000000000002 = <diffusion2d.SolveDiffusion2D object at 0x0000015A4DE3E420>.dt

tests\integration\test_diffusion2d.py:22: AssertionError
------------------------------------------------------------------------ Captured stdout call -------------------------------------------------------------------------
dt = 0.010000000000000002
========================================================================== warnings summary ===========================================================================
..\..\..\..\..\..\..\..\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37
  C:\Users\Vedant\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37: DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
    EPOCH = datetime.datetime.utcfromtimestamp(0)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================= short test summary info ======================================================================= 
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.01 == 0.008
=============================================================== 1 failed, 1 passed, 1 warning in 0.92s ================================================================ 
```

#### Changing to `u = self.T_hot * np.ones((self.nx, self.ny))` in set_initial_condition

```sh
PS C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425> python -m pytest .\tests\integration\test_diffusion2d.py
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.12.0, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Vedant\Documents\Uni\Subjects\Winter2425\SimTech\Exercises\Exercise7\testing-python-exercise-wt2425
collected 2 items

tests\integration\test_diffusion2d.py .F                                                                                                                         [100%]

============================================================================== FAILURES ===============================================================================
_____________________________________________________________________ test_set_initial_condition ______________________________________________________________________

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
>       np.testing.assert_array_equal(u, u_expected, "Expected array:\n{}\nGot:\n{}\n".format(u_expected, u))

tests\integration\test_diffusion2d.py:45: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

args = (<built-in function eq>, array([[500., 500., 500., 500., 500.],
       [500., 500., 500., 500., 500.],
       [500., 5... array([[200., 200., 200., 200., 200.],
       [200., 200., 200., 200., 200.],
       [200., 200., 200., 200., 200.]]))
kwds = {'err_msg': 'Expected array:\n[[200. 200. 200. 200. 200.]\n [200. 200. 200. 200. 200.]\n [200. 200. 200. 200. 200.]]\n.... 500. 500. 500.]\n [500. 500. 500. 500. 500.]]\n', 'header': 'Arrays are not equal', 'strict': False, 'verbose': True}

    @wraps(func)
    def inner(*args, **kwds):
        with self._recreate_cm():
>           return func(*args, **kwds)
E           AssertionError: 
E           Arrays are not equal
E           Expected array:
E           [[200. 200. 200. 200. 200.]
E            [200. 200. 200. 200. 200.]
E            [200. 200. 200. 200. 200.]]
E           Got:
E           [[500. 500. 500. 500. 500.]
E            [500. 500. 500. 500. 500.]
E            [500. 500. 500. 500. 500.]]
E
E           Mismatched elements: 15 / 15 (100%)
E           Max absolute difference: 300.
E           Max relative difference: 1.5
E            x: array([[500., 500., 500., 500., 500.],
E                  [500., 500., 500., 500., 500.],
E                  [500., 500., 500., 500., 500.]])
E            y: array([[200., 200., 200., 200., 200.],
E                  [200., 200., 200., 200., 200.],
E                  [200., 200., 200., 200., 200.]])

C:\Program Files\Python312\Lib\contextlib.py:81: AssertionError
------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------- 
dt = 0.05
========================================================================== warnings summary =========================================================================== 
..\..\..\..\..\..\..\..\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37
  C:\Users\Vedant\AppData\Roaming\Python\Python312\site-packages\dateutil\tz\tz.py:37: DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
    EPOCH = datetime.datetime.utcfromtimestamp(0)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================= short test summary info =======================================================================
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError:
=============================================================== 1 failed, 1 passed, 1 warning in 0.97s ================================================================ 
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
