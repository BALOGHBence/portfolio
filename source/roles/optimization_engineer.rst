==============================
Me as an Optimization Engineer
==============================

As someone coming from theoretical solid mechanics, I'm naturally drawn to optimization problems, as **classical mechanics is
the traditional field of application of optimization**. As the laws of nature are governed by extremum principles, **it is 
impossible to be well trained in any field of theoretical physics without having a firm understanding of optimization**.
Simply put, optimization is 'business as usual' for someone in computational solid mechanics, part of everyday life.

Let me tell you an example. When we calculate the deflection of a beam, we are actually solving an optimization problem, and
we use the principle of minimum potential energy to do so. We formulate the expression for the potential energy, and we
calculate the value of the arguments that would minimize the expression. The supports defined on a structure are in fact
constraints, and the problem becomes a nonlinear, constrained optimization problem. In general, what we do in solid mechanics
is that we produce approximate solutions to partial differential equations (PDEs). We to that by constructing functions with
lots of unknown parameters, establish an error measure, and we calculate the unknowns in a way so that the error of the
approximation is minimal from all the possible options.

But there is more.

My field of study as a PhD student was Structural Topology Optimization, which is about figuring out
what shape should a structure have in order to maximize it's performance. It is about optimizing the
mass distribution of a structure, subject to various constraints, to improve on the performance of it. 
This work required not only a solid understanding of solid mechanics but also a deep knowledge of optimization algorithms, 
both theoretical and practical. **I have hands-on experience with gradient-based and gradient-free optimization algorithms, heuristic 
and path-following methods, linear and nonlinear, as well as integer and real-valued optimization problems.** Most of these
methods I've implemented myself.
As a result of my work, I've developed a custom, domain-specific optimization algorithm to solve the topology optimization problem, a highly nonlinear, 
mixed-integer problem with PDE constraints. This problem is beyond the capabilities of even the most advanced libraries 
like Gurobi or CPLEX, necessitating a deep understanding of the problem and the ability to create a custom solution. My algorithm 
for finding optimal topologies required a thorough comprehension of the problem's unique properties, allowing me to craft 
domain-specific solutions that leverage these characteristics. **I think that this knowledge is far more valuable 
than simply knowing how to use existing libraries like Gurobi or CPLEX.** What happens if the problem is out
of reach for these libraries, like it was the case with my topology optimization problem? Then, you have to come up with
a dedicated solution to the problem, like I did, and this is where the real fun begins, this is where fundamental
understanding of the field is key.

The algorithms I've implemented myself so far are:

* A **graph theory-based optimization algorithm** to minimize the bandwidth of the coefficient matrix in a finite element software.

* A **meta-heuristic binary genetic algorithm** for general purpose nonlinear optimization.

* A **solver for linear programming problems (LPP) of all kinds** including continuous and mixed-integer problems.

* A high performance **topology optimization algorithm** using an Optimality Criteria Method (OC) using the SIMP approach for:
  
  * Finding the optimal topology of general structures for minimum volume, subject to an upper bound
    constraint on the work of external forces, a PDE constraint expressing the equilibrium,
    and an upper bound constraint on the utilization of the structure.
  
  * Finding the optimal topology of general structures for maximum stiffness, subject to an upper bound
    constraint on the volume, a PDE constraint expressing the equilibrium,
    and an upper bound constraint on the utilization of the structure.

  * **Handling millions of design variables efficiently**, and being applicable to general structural models
    (models including 1D, 2D, and 3D domains).

* A shape optimization algorithm to optimize various kinds of curved-folded structures using the
  Finite Strip Method (FSM) for minimum weight, subject to an upper bound constraint on the volume,
  a PDE constraint expressing the equilibrium of the strucrure.

For the first tree, you can find program code in my open-source library `sigmaepsilon.math`, introduced
in this project:

:ref:`Development of a Scientific Research Toolkit in Python Including a Finite Element and a Tensor Algebra Library`

To read about the solution for linear programming problems, you can visit this project:

:ref:`Development of a Software Solution for Linear Programming Problems in Python`

The most complex one of these is by far the topology optimization algorithm, which, trust me, is probably more challenging
than any you might present to me. You can read more about it here:

:ref:`Development of a High Performance Topology Optimization Library in Python`

Let me end this section with a quote from the famous mathematician, Leonhard Euler:

.. epigraph::

   "Nothing takes place in the world whose meaning is not that of some maximum or minimum."

   ~ Leonhard Euler

What this means is that every problem can be formulated as an optimization problem. I understand why Euler said this, and I
actually solve a lot of problems by first transforming them into optimization problems. This is the way I think, this is the
way I work, and this is the way I can help you. **You tell me a problem, and I can formulate that problem 
as an optimization problem, and I can solve it.**
