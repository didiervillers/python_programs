# -*- coding: utf-8 -*-
"""
In the introduction of his MOOC "SMAC" (Statistical Mechanics: Algorithms and
Computations - https://www.coursera.org/learn/statistical-mechanics), Werner
Krauth propose a simple method to compute pi using a direct sampling
Monte Carlo simulation. A program is proposed in Python, in a version which
allows to do many runs of the function direct_pi(N). The code is written in a
style close to pseudocode used for algorithms, or classical coding style used
in C, Fortran,...

It is possible to write the function in a more "pythonic" way, or to use the
numpy numerical library, to improve compactness and efficiency.

Function direct_pi_DV(N) use pure python with list comprehension to eliminate
the for loop. The sum is directly made on the boolean comparison results to count
the number of true trials.

Function direct_pi_DV_np(N) use the numpy library to vectorize the loop, directly
square values and sum the array elements over the smaller axis. Again the sum
is directly made on the boolean comparisons.

Finally, in order to compare efficiency, the execution times of the three
versions have been measured using the timeit library.

Here is value obtain for a sample run :
direct_pi       : 3.5209695600005944 s
direct_pi_DV    : 4.000994963998892 s
direct_pi_Dv_np : 0.19237353700009407 s

The use ot the numpy library clearly improve the computer speed performance by
a factor about 20.
"""
import random, timeit
import numpy as np
 
def direct_pi(N):
    n_hits = 0
    for i in range(N):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x ** 2 + y ** 2 < 1.0:
            n_hits += 1
    return n_hits

def direct_pi_DV(N):
    return sum((random.uniform(-1,1)**2 + random.uniform(-1,1)**2) < 1 for i in range(N))
 
def direct_pi_DV_np(N):
    return np.sum((np.random.uniform(-1,1,(N,2))**2).sum(1)<1)

n_runs = 1000
n_trials = 4000

# running :
for run in range(n_runs):
    print(run, 4.0 * direct_pi(n_trials) / n_trials)

for run in range(n_runs):
    print(run, 4.0 * direct_pi_DV(n_trials) / n_trials)

for run in range(n_runs):
    print(run, 4.0 * direct_pi_DV_np(n_trials) / n_trials)

# timing three versions :
print(timeit.timeit('direct_pi('+str(n_trials)+')', "from __main__ import direct_pi", number=n_runs))
print(timeit.timeit('direct_pi_DV('+str(n_trials)+')', "from __main__ import direct_pi_DV", number=n_runs))
print(timeit.timeit('direct_pi_DV_np('+str(n_trials)+')', "from __main__ import direct_pi_DV_np", number=n_runs))
