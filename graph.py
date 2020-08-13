import matplotlib.pyplot as plt

def displaystoptimesGraph(y):

    plt.title('Collatz')
    plt.xlabel('Number')
    plt.ylabel('Stoptime')
    plt.scatter(range(1, len(y) + 1), y)

    plt.plot()
    plt.show()