==============================================================================================================
Development of a Scientific Research Toolkit in Python Including a Finite Element and a Tensor Algebra Library
==============================================================================================================

Keywords
========

Python, Finite Element Analysis, Research, Linear Algebra, Tensor Algebra, Scientific Computing, Software Development

Overview
========

I’m a self-taught programmer and software developer. At the beginning of my journey, I just wrote code to support my 
scientific endeavors. Code snippets all around the place for article after article. It was a big mess. After some time, 
I started to organize my work so that the different pieces come together into an ecosystem of tools. Some of my work is 
open-source and freely available to the public, some are not. Also, unfortunately, I had to leave university and abandon 
my PhD studies, as the humiliating salary of 300 EUR/month (no typo there, this is real data from 2019) just wasn’t enough, 
even for basic needs. I quickly realized that expensive software like MatLab and Mathematica could only serve me until I 
was there. Now, I can conduct research in my field all by myself using the tools that I wrote and the sea of other things 
the open-source community provides and I’m proud of the fact that I also contribute to the community. My most notable 
contribution can be found under the namespace `sigmaepsilon`, which consists of a collection of namespace packages, 
the most important ones being

- `sigmaepsilon.math <https://pypi.org/project/sigmaepsilon.math/>`_: This library includes a full-fledged tensor 
  algebra library. I’m talking about real tensors here, not just multidimensional arrays as it is commonly misunderstood 
  in data science. It also includes solutions for optimization, approximation, regression, and calculations related to 
  graph theory.
- `sigmaepsilon.mesh <https://pypi.org/project/sigmaepsilon.mesh/>`_: This library is about managing, manipulating, and storing 
  data related to meshes. It is a key component for my finite element library as it provides the base classes 
  (geometrical discretization) for most of the isoparametric finite elements.
- `sigmaepsilon.solid.material <https://pypi.org/project/sigmaepsilon.solid.material/>`_: This library is about managing 
  material data. It includes solutions for the calculation of material properties, stress-strain relations, and 
  constitutive models. It is a key component for my finite element library as it provides the material models for 
  the elements.
- `sigmaepsilon.solid.fourier <https://pypi.org/project/sigmaepsilon.solid.fourier/>`_: This library is about semi-analytical
  solutions for simple plate problems. It is great for educational purposes, idea validation and verification of solutions
  coming from fully numerical soliutions, like the finite element method.

All the libraries listed here are professional Python packages, with documentation, tests, and continuous integration,
build along sommmunity standards. They are also available on the Python Package Index (PyPI) and can be installed using
pip. The source code is available on GitHub, and the documentation is hosted on Read the Docs.

These libraries are key in my development as a Python programmer, this is where I learned the most. Here, I can go down 
the rabbit hole as far as I wish without any limitations. I can implement the most advanced algorithms, I can experiment
with new ideas, and I can learn from my mistakes. This is where I can practice my creativity.
