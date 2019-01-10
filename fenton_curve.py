import matplotlib.pyplot as plt
import numpy as np
with plt.xkcd():
    # Based on matplotlib example
    
    vals_x = np.linspace(0,18,100)
    fig = plt.figure()
    ax = fig.add_axes((0.15, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    #plt.xticks([])
    #plt.yticks([])
    ax.set_ylim([0, 1.1])

    data = 1/(1+np.sqrt(np.exp(9-vals_x)))

    plt.annotate(
        'We\'re here',
        xy=(0.2, 0.05), arrowprops=dict(arrowstyle='->'), xytext=(1, 1))

    plt.plot(vals_x,data)

    plt.xlabel('months from now')
    plt.ylabel('normalized python adoption')
    plt.show()