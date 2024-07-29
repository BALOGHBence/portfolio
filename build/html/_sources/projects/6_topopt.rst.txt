.. _Development of a High Performance Topology Optimization Library in Python:

=========================================================================
Development of a High Performance Topology Optimization Library in Python
=========================================================================

Keywords
========

Python, Finite Element Analysis, Research, Linear Algebra, Tensor Algebra, Scientific Computing, Software Development,
Topology Optimization, Structural Analysis

Overview
========

When I started my PhD studies at the Department of Structural Mechanics @ BUTE, I was using Delphi as my daily driver 
when it came to general tasks. The reason behind this choice is that I was already working for Inter-CAD at the time 
and this is the language they use to develop AxisVM. I quickly realized that Delphi has weak tooling, and I struggled 
with visualization in 3D, so I turned my attention to Python and this is the language I’m using to develop my topology 
optimization library ever since. In my opinion, it is a perfect blend of speed and productivity. I started the development 
from scratch, I received nothing from my supervisor or other members of the department, and I had to do it all by myself. 
I even implemented the finite element library and the equation solver myself. The reason for implementing an equation 
solver was that I had a computer with only 4 GB of RAM, which was simply not enough to satisfy the needs of my computations. 
As a solution, I implemented a special kind of equation solver, a frontal method. This method is known to run on the smallest 
of memories. It was slow compared to other solvers, but it worked perfectly. It was so slow, that I also had to implement 
King’s algorithm to optimize the numbering of the finite elements to achieve a stiffness matrix with minimum bandwidth, 
resulting in the smallest possible front-size, that is the smallest memory footprint. Now, I have a solution that can 
optimize the mass distribution of any kind of structure for either minimum weight or maximum stiffness, subject to arbitrary 
utilization constraints. The main characteristics of the solution are the ability to handle an extremely large number of 
design variables efficiently and its applicability to general structural models (models including 1s, 2d, and 3d domains). 
The performance and capabilities of the solution are comparable with the ones included in professional software such as 
Fusion360 or SolidWorks. The library builds on the ecosystem under the name sigmaepsilon, which is a set of tools I have 
developed to create an ideal environment for my research purposes and self-development.

.. figure:: ../_static/topopt_compound.png
   :align: center
   
   The initial and optimized structure, including 1d, 2d and 3d domains. The statical model is a console with
   a point load at the free end.
