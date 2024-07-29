==============================
Me as an Optimization Engineer
==============================

I was introduced to the field of optimization during my PhD studies, where I focused on the optimal design of structures. 
This work required not only a solid understanding of solid mechanics but also a deep knowledge of optimization algorithms, 
both theoretical and practical. I have experience with gradient-based and gradient-free optimization algorithms, heuristic 
and path-following methods, and linear and nonlinear, as well as integer and real-valued optimization problems.

During my PhD, I developed a custom optimization algorithm to solve the topology optimization problem, a highly nonlinear, 
mixed-integer optimization challenge with PDE constraints. This problem is beyond the capabilities of even advanced libraries 
like Gurobi or CPLEX, necessitating a deep understanding of the problem and the ability to create a custom solution. My algorithm 
for finding optimal topologies required a thorough comprehension of the problem's unique properties, allowing me to craft 
domain-specific solutions that leverage these characteristics. I believe that this specialized knowledge is far more valuable 
than simply knowing how to use existing libraries.

The algorithms I've implemented myself so far are:

* A graph theory-based optimization algorithm to minimize the bandwidth of the coefficient matrix in a finite element software.

* A genetic algorithm for general purpose nonlinear optimization.

* A solve for linear programming problems (LPP) of all kinds.

* A topology optimization algorithm using an Optimality Criteria Method (OC) using the SIMP approach for:
  
  * Finding the optimal topology of general structures for minimum volume, subject to an upper bound
    constraint on the work of external forces, a PDE constraint expressing the equilibrium,
    and an upper bound constraint on the utilization of the structure.
  
  * Finding the optimal topology of general structures for maximum stiffness, subject to an upper bound
    constraint on the volume, a PDE constraint expressing the equilibrium,
    and an upper bound constraint on the utilization of the structure.

* A shape optimization algorithm to optimize various kinds of curved-folded structures using the
  Finite Strip Method (FSM) for minimum weight, subject to an upper bound constraint on the volume,
  a PDE constraint expressing the equilibrium of the strucrure.