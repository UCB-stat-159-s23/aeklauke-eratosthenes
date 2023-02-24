import matplotlib.pyplot as plt

def plot_sieve(p, log_scale = True):
    plt.plot(p[0], p[1])
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")
    if log_scale == True:
        plt.xscale("log")
        plt.yscale("log")   
