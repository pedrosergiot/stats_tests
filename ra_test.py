__all__ = ["ra"]

import numpy as np
from scipy.stats import norm


def ra(x):

    """ Executes the reverse arrangements test for a certain alpha level (significance level)
        Returns 1 for rejection of the null hypothesis and zero for not rejected

        Implementation according to Random Analysis and Measurement Procedures - Bendat and Piersol"""

    # store the results of the test
    ra_dict = {}

    # number of samples
    N = len(x)

    # mean and standard deviation for the distribution of A (number of reverse arrangements)
    mean_A = N * (N - 1) / 4
    std_A = np.sqrt(N * (2 * N + 5) * (N - 1) / 72)

    # number of reverse arrangements
    A = 0

    # loop for calculation of A
    for i in range(0, N):
        for j in range(i + 1, N):

            if x[i] > x[j]:
                A += 1

    # z-score for the value of reverse arrangements obtained
    z_score = (A - mean_A) / std_A

    # store the z_score
    ra_dict[0] = z_score

    # store the p-value associated to the z-score obtained
    ra_dict[1] = norm.cdf(z_score)

    # store the critical values for the reverse arrangements test
    crit_dict = {'1%': (norm.ppf(0.01 / 2), norm.ppf(1 - 0.01 / 2)),
                 '5%': (norm.ppf(0.05 / 2), norm.ppf(1 - 0.05 / 2)),
                 '10%': (norm.ppf(0.10 / 2), norm.ppf(1 - 0.10 / 2))}

    ra_dict[2] = crit_dict

    return ra_dict