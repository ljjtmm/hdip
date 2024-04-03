import matplotlib.pyplot as plt
import numpy as np

def main():
    #Generate normal distribution data
    mean = 5
    stddev = 2

    data = np.random.normal(mean, stddev, 1000)

    #Generate data for function
    x = np.linspace(0, 10, 100)
    y=  x**3

    #Create historgram
    plt.hist(data, bins=30, alpha=0.5, color='skyblue', edgecolor='black', label="Normal distribution")

    #Plot the function
    plt.plot(x, y, label = "$h(x)=x^3$", color = "red")

    #Legends and axes
    plt.legend()
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.title("Histogram of Normal Distribution and Plot of $h(x) = x^3$")

    plt.ylim(0, max(max(plt.hist(data, bins=30, density=True)[0]), max(y)))

    #Show our plot
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()