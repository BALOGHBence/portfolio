.. _Research and Software Implementation of a Novel Design Module for Multi-Layered Composite Shells in AxisVM:

==========================================================================================================
Research and Software Implementation of a Novel Design Module for Multi-Layered Composite Shells in AxisVM
==========================================================================================================

Keywords
========

Delphi, Finite Element Analysis, Composite Mechanics, Research, Software Development, Structural Analysis

Overview
========

.. sidebar::
   
   .. figure:: ../_static/xlam.png
      :align: center
      :height: 200

      An XLAM plate with multiple layers.

During my time at `AxisVM <https://axisvm.eu/>`_, one of my duties was to create a design module capable of handling XLAM plates, 
which are multi-layered timber plates. The task was very challenging since Eurocode (the collection of standards 
related to the design of civil engineering structures) was completely silent on the matter. It had chapters for 
timber beams, but it doesn’t follow from that. It was my task to figure out the metrics to be used and to do all 
software development from calculation to UI design. The responsibility was enormous because I knew that end users 
would trust my metrics and they would rely on the product to design actual structures. I did my research and I came 
up with an implementation, which was an industry-leading solution at the time. It was not a copy of existing solutions, 
but an original approach to the problem.

.. figure:: ../_static/xlam_stresses.png
   :align: center
   
   The visualization I created for the stress distribution.


.. raw:: html

    <p class="p-centralized">
        <a href="../_static/axisvm_xlam_guide_en.pdf" target="_blank">
            <button class="fancy-download-button">Click here to see the full documentation of the module.</button>
        </a>
    </p>
   
   
Features
========

- **Calculation of equivalent model stiffness matrices for arbitrary multi-layered shells:** The implemented
  solution is capable of calculating the stiffness matrix of any kind of multi-layered shell, including, but not 
  limited to XLAM plates. The calculation also includes the determination of shear correction factors for 
  Uflyand-Mindlin plates.
- **Graphical visualization of stress distribution:** The software provides a graphical representation of the stress
  distribution in the plate, allowing engineers to visualize the load paths and stress concentrations.

Technologies Used
=================

- **Delphi:** Core programming language for developing the algorithms used in AxisVM.
- **ANSYS APDL:** I used ANSYS to validate my results. I created a model in ANSYS and compared the results with my own implementation.
- **LaTeX:** Used for the documentation of the design module (click on the button above to see it).

Challenges and Solutions
========================

- **Absence of existing solutions:** When I was given the task, Eurocode was completely silent on the matter of timber plates; the existing solutions
  were based on beam solutions. I had to do my own research and come up with a solution that was compliant
  with the existing standards, but also provided a reliable and accurate solution for the design of timber plates. This required a deep
  understanding of composite mechanics, finite element analysis, and software development. The final solution is based on shell theory
  insted of beam theory, which was a novel approach at the time.
- **Huge responsibility:** I knew that when the product was going to be launched into production, engineers all around Europe would rely
  on it and trust the tools we provide for them. This was a huge responsibility, and I had to make sure that the solution was accurate,
  which in the absence of standards or experiments, was a challenging task. I had to validate my results using analytical solutions and ANSYS.

Conclusion
==========

Overall, this project highlights my capacity for original research, creative problem-solving, and the practical application of complex engineering principles.
It shows that I'm able to take and critically investigate existing approaches to a problem and improve upon them when necessary.
It exemplifies my dedication to developing reliable, accurate, and user-friendly tools that advance the field of structural analysis and design, while 
performing exceptionally well under significant responsibility and pressure.
