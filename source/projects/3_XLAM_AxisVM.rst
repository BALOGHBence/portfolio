===========================================================================================
Research and Implementation of a Design Module for Multi-Layered Composite Shells in AxisVM
===========================================================================================

Keywords
========

Delphi, Finite Element Analysis, Composite Mechanics, Research, Software Development, Structural Analysis

Overview
========

During my time at `AxisVM <https://axisvm.eu/>`, one of my duties was to create a design module capable of handling XLAM plates, 
which are multi-layered timber plates. The task was very challenging since Eurocode (the collection of standards 
related to the design of civil engineering structures) was completely silent on the matter. It had chapters for 
timber beams, but it doesn’t follow from that. It was my task to figure out the metrics to be used and to do all 
software development from calculation to UI design. The responsibility was enormous because I knew that end users 
would trust my metrics and they would rely on the product to design actual structures. I did my research and I came 
up with an implementation, which was an industry-leading solution at the time. It was not a copy of existing solutions, 
but an original approach to the problem.

.. figure:: ../_static/homogenization_1.png
   :align: center
   
   Illustration of the homogenization process for a ribbed plate.
   
   
Features
========

- **Automatic calculation of equivalent model stiffness matrices:** The algorithm is capable to determining
  equivalent stiffness matrices of partcically any kind of shell with a periodic microstructure. A key feature of the
  solution is the ability to handle the most complex of geometries and material properties. It uses a 3d RVE and
  determines the stiffness matrix for a 2d model using a retrofitting approach, which is an original contribution.

Technologies Used
=================

- **Delphi:** Core programming language for developing the algorithms used in AxisVM.
- **Finite Element Analysis:** Utilized for the numerical solution of the homogenization equations.
- **Optimization Techniques:** Implemented to improve the efficiency and accuracy of the calculations.
- **Frontal Method Solver:** Developed for solving the linear systems of equations arising from the homogenization process.
- **Graph Theory-Based Optimization:** Used to minimize the bandwidth of the coefficient matrix for improved computational efficiency,
  falling in the category of combinatorial optimization.

Challenges and Solutions
========================

- **Standalone Implementation:** Using legacy code was not an option due to technical difficulties. Therefore, the 
  implementation comes with it's own finite elements, equation solver, pre- and postprocessing
  tools, etc. This also involves the implementation of a direct equation solver (frontal method), accompanied by an 
  optimizer that renumbers the elements such that the coefficient matrix has minimal bandwidth. Here I implemented King's 
  method.
- **Mathematical Complexity:** The theory behind the solution is based on advanced mathematical concepts, such as 
  two-scale asymptotic expansion, differential equations and retrofitting. Implementing these concepts in a practical software 
  tool required a deep understanding of both the theoretical and computational aspects. I had to develop a robust algorithm that 
  could handle the complexity of the calculations while maintaining efficiency and accuracy. This involved extensive testing and 
  validation to ensure the correctness of the results.

Conclusion
==========

The project showcases my abilities in theoretical research, algorithm development, and software implementation and problem 
solving in general. It is one thing to read a book and implement the algorithms described in it, but it is a completely different 
challenge to take an existing theory and improve it, makeing it more suitable to a given problem. This requires a deep understanding
of the underlying principles, as well as creativity and problem-solving skills.
