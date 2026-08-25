import matplotlib.pyplot as plt
from functions import *

seed = int(input("Enter seed value: "))
set_seed(seed)

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
N = int(input("Enter number of samples: "))

uniform_values = generate_uniform(a, b, N)

plt.hist(uniform_values, bins=30, edgecolor="black")
plt.title("Uniform Random Variables")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

mu = float(input("Enter mean: "))
sigma = float(input("Enter standard deviation: "))

gaussian_values = generate_gaussian(mu, sigma, N)

plt.hist(gaussian_values, bins=30, edgecolor="black")
plt.title("Gaussian Random Variables")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

mean, variance = calculate_statistics(gaussian_values)

required_variance = sigma * sigma
mean_error = abs(mean - mu)
variance_error = abs(variance - required_variance)
total_error = mean_error + variance_error

print("Given Mean =", mu)
print("Generated Mean =", mean)
print("Given Variance =", required_variance)
print("Generated Variance =", variance)
print("Mean Error =", mean_error)
print("Variance Error =", variance_error)
print("Total Error =", total_error)