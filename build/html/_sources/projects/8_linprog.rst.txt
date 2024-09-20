.. _Development of a Software Solution for Linear Programming Problems in Python:

============================================================================
Development of a Software Solution for Linear Programming Problems in Python
============================================================================

Keywords
========

Python, Optimization, Linear Programming, Software Development, Algorithm Development, Numerical Methods

Overview
========

I developed a software solution for solving linear programming problems in Python. It efficiently handles a 
variety of problem types, including both continuous and mixed-integer linear programming. What sets my 
solution apart from other available options is its ease of use without compromising performance. Users 
can define problems naturally, without needing to conform to the specific formats required by most solvers. 
The library provides a unified and straightforward interface for setting up and solving linear programming problems.

Visit the `documentation <https://sigmaepsilonmath.readthedocs.io/en/latest/user_guide/optimization.html>`_ 
to see more details about the solution.


.. code-block:: python

    from sigmaepsilon.math.optimize import LinearProgrammingProblem as LPP
    import sympy as sy

    x1, x2, x3, x4 = variables = sy.symbols(['x1', 'x2', 'x3', 'x4'])
    obj = Function(3*x1 + 9*x3 + x2 + x4, variables=variables)
    eq1 = Relation(x1 + 2*x3 + x4 - 4, variables=variables)
    eq2 = Relation(x2 + x3 - x4 - 2, variables=variables)
    bounds = [(0, None), (0, None), (0, None), (0, None)]
    lpp = LPP(obj, [eq1, eq2], variables=variables, bounds=bounds)
    solution = lpp.solve()


