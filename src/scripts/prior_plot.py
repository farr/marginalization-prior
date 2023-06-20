import matplotlib.pyplot as plt
import numpy as np
import paths
import scipy.special as ss

def pa(n, a):
    return ss.gamma((n-1)/2)*ss.gammaincc((n-1)/2, np.square(a)/2)/(np.sqrt(2)*ss.gamma(n/2))

if __name__ == '__main__':
    xs = np.linspace(0, 3, 1024)
    n = np.array([2, 4, 8])

    for i in n:
        plt.plot(xs, pa(i, xs), label=r'$n = {}$'.format(i))
    plt.legend()
    plt.xlabel(r'$a / a_\mathrm{max}$')
    plt.ylabel(r'$p\left( a / a_\mathrm{max} \right)$')

    plt.tight_layout()
    plt.savefig(paths.figures / 'prior_plot.pdf')