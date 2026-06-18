.. index:: simulation; Monte Carlo, Monte Carlo method, random number; simulation,
           pi estimation; Monte Carlo, probability; simulation
   ACM-IEEE CS2013; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2023; SDF2 Fundamental Programming Concepts
   ACM-IEEE CS2013; AL2 Algorithmic Strategies
   ACM-IEEE CS2023; AL2 Algorithmic Strategies
   ACM-IEEE CS2013; DS6 Discrete Probability
   ACM-IEEE CS2023; DS6 Discrete Probability

.. _Monte-Carlo-Simulation:

Monte Carlo Simulation
=======================

.. note::
   *Source:* Adapted from `scalaworkshop
   <https://github.com/gkthiruvathukal/scalaworkshop>`_
   by George K. Thiruvathukal and Konstantin Läufer.

A *simulation* uses a computer to model a process that would be
expensive, slow, or impossible to run in the real world.  *Monte Carlo
simulation* is a family of techniques that use random sampling to
estimate numerical results.  The name comes from the Monte Carlo casino
in Monaco — randomness is the engine.

.. index:: Monte Carlo method; concept, random sampling; estimation

The Monte Carlo Method
-----------------------

The core idea is simple: if you cannot compute an answer exactly, throw
a lot of random samples at the problem and see what fraction satisfy your
criterion.  The fraction converges to the true probability (or area, or
integral) as the number of samples grows.

A classic example is estimating the area of a unit circle — and
therefore π — by throwing random "darts."

.. index:: pi estimation; dart throwing, unit circle; Monte Carlo

Estimating π with Darts
------------------------

Imagine a 2×2 square centred at the origin, with a unit circle (radius
1) inscribed inside it.  The area of the square is 4; the area of the
circle is π.  If you throw darts uniformly at random at the square, the
fraction that land inside the circle is π/4.  Multiply by 4 to get π.

.. code-block:: none

   P(dart inside circle) = area of circle / area of square = π / 4

   Therefore: π ≈ 4 × (darts inside) / (total darts)

.. index:: random.uniform; simulation, generate_darts

Generating Darts
^^^^^^^^^^^^^^^^^

Each dart is a random point (x, y) with x and y drawn uniformly from
[-1, 1].  A dart is *inside* the circle when x² + y² ≤ 1:

.. literalinclude:: ../../examples/introcs-python/simulation/monte_carlo.py
   :language: python
   :start-after: # start: generate_darts
   :end-before: # end: generate_darts

The function returns a list of dictionaries, one per dart, with keys
``x``, ``y``, and ``inside``.  Using a dictionary makes the data
self-describing and easy to save to CSV later.

Estimating π
^^^^^^^^^^^^^

.. literalinclude:: ../../examples/introcs-python/simulation/monte_carlo.py
   :language: python
   :start-after: # start: estimate_pi
   :end-before: # end: estimate_pi

Counting the darts inside and applying the formula gives the estimate.
With 100 000 darts a typical run produces:

.. code-block:: python

   import math
   darts = generate_darts(100_000)
   print(f"π ≈ {estimate_pi(darts):.6f}  (true: {math.pi:.6f})")

Output:

.. code-block:: none

   π ≈ 3.141440  (true: 3.141593)

Here is a complete, self-contained version you can run right now.  We seed
the generator with ``random.seed(0)`` so the output is reproducible; remove
that line and run it several times to watch the estimate change.  Increase
``n`` and watch the estimate settle closer to π:

.. try_examples::
   :height: 340

   >>> import math
   >>> import random
   >>> random.seed(0)
   >>> def estimate_pi(n):
   ...     inside = 0
   ...     for _ in range(n):
   ...         x = random.uniform(-1, 1)
   ...         y = random.uniform(-1, 1)
   ...         if x * x + y * y <= 1:
   ...             inside += 1
   ...     return 4 * inside / n
   ...
   >>> for n in [100, 1_000, 10_000, 100_000]:
   ...     est = estimate_pi(n)
   ...     print(f"n={n:>7}: pi ~= {est:.5f}  error={abs(est - math.pi):.5f}")
   ...
   n=    100: pi ~= 3.28000  error=0.13841
   n=   1000: pi ~= 3.02000  error=0.12159
   n=  10000: pi ~= 3.14480  error=0.00321
   n= 100000: pi ~= 3.13056  error=0.01103

Saving Darts to CSV
^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/introcs-python/simulation/monte_carlo.py
   :language: python
   :start-after: # start: save_darts
   :end-before: # end: save_darts

``csv.DictWriter`` writes each dart dictionary as one row, with the keys
becoming column headers.  The saved file can be reloaded for later
analysis or shared with other programs.

.. index:: convergence; Monte Carlo, law of large numbers

How Accuracy Improves with N
-----------------------------

The estimate improves as n grows, following the *law of large numbers*:
each time you multiply n by 10 the error roughly shrinks by a factor of
√10 ≈ 3.16.  The function below prints the estimate and its absolute
error at several scales:

.. literalinclude:: ../../examples/introcs-python/simulation/monte_carlo.py
   :language: python
   :start-after: # start: convergence
   :end-before: # end: convergence

.. code-block:: python

   convergence_table([100, 1_000, 10_000, 100_000, 1_000_000])

Output (results vary due to randomness — typical run):

.. code-block:: none

            n    π estimate       error
   --------------------------------------
         100    3.120000    0.021593
       1,000    3.144000    0.002407
      10,000    3.138800    0.002793
     100,000    3.141440    0.000153
   1,000,000    3.141612    0.000019

Each tenfold increase in darts roughly halves the error — the price of
one more decimal place is 100× more work.

.. index:: matplotlib; scatter plot, scatter plot; Monte Carlo

Visualizing the Simulation
---------------------------

A scatter plot shows exactly where the darts land, with the boundary
circle drawn over them.  Blue dots are inside the circle; red are
outside:

.. literalinclude:: ../../examples/introcs-python/simulation/monte_carlo_plot.py
   :language: python
   :start-after: # start: plot_darts
   :end-before: # end: plot_darts

.. code-block:: python

   from monte_carlo import generate_darts
   darts = generate_darts(20_000)
   plot_darts(darts, 'darts.png')

Install ``matplotlib`` if needed:

.. code-block:: none

   pip install matplotlib

The resulting image shows the quarter-circles of blue darts filling the
circle while the red darts occupy the corners of the square, making the
geometry of the estimate immediately visible.

.. index:: simulation; applications, Monte Carlo; real-world applications

Where Monte Carlo Is Used
--------------------------

Monte Carlo methods power calculations across science and engineering:

- **Physics** — particle collisions, nuclear reactions, radiation transport
- **Finance** — option pricing, risk analysis (Value at Risk)
- **Climate modelling** — uncertainty quantification in weather forecasts
- **Computer graphics** — path tracing for photorealistic rendering
- **Machine learning** — dropout regularisation, Bayesian inference

The idea is always the same: replace an intractable exact computation
with a large number of cheap random samples.

Exercises
---------

1. Run ``convergence_table([100, 1_000, 10_000, 100_000])`` several
   times.  Does the error always decrease monotonically?  Why or why not?

2. Modify ``generate_darts`` to accept a ``seed`` parameter and pass it
   to ``random.seed`` before the loop.  Verify that two calls with the
   same seed produce identical results.

3. The unit circle has area π.  Use the same dart-throwing technique to
   estimate the area of a unit square rotated 45° (a diamond with
   vertices at (±1, 0) and (0, ±1)).  What should the answer be?

4. Write a function ``estimate_pi_from_csv(filename)`` that reads a
   darts CSV saved by ``save_darts`` and returns the pi estimate without
   regenerating the darts.

5. Plot how the absolute error changes as n increases from 100 to
   1 000 000 (use a logarithmic x-axis).  Does the slope of the error
   curve match the expected –½ on a log-log scale?
