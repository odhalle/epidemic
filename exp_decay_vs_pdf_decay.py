import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

if __name__ == '__main__':
    delta = .001  # for resolution
    decay_rate = .15  # for exponential model
    mean = 5.  # mean nb of days before leaving the group
    sigma = 2.5  # sigma before leaving the group
    prob1 = stats.norm.pdf(np.arange(0, 14 / delta, 1), mean / delta, sigma / delta)  # pdf of going leaving the group
    group_0 = 1000  # initial condition
    group = [group_0]
    group_prob = [group_0]

    # Assume that 1000 just entered the group at beginning
    group_j = np.zeros(int(14 / delta))
    group_j[0] = group_0
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        group_j[i] = 100
    print(group_j)
    x_ = np.arange(0., 20., delta)
    dt = x_[1] - x_[0]
    for i in x_[1:]:
        next_group = group[-1] - decay_rate * group[-1] * dt
        next_group_prob = group_prob[-1] - np.sum(prob1 * group_j)
        group.append(next_group)
        group_prob.append(next_group_prob)
        # update group_j for next delta time
        group_j = np.insert(group_j, 0, 0)
        group_j = np.delete(group_j, -1)

    # As we choose a normal law and with the initial conditions, number of people will follow a normal profile
    plt.plot(x_, group)
    plt.plot(x_, group_prob)
    plt.show()
