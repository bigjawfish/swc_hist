#  Randomizing data, generating summary statistics, and histogram
import numpy as np
import matplotlib.pyplot as plt

mu = 80
sigma = 10

x = np.random.normal(mu,sigma,100)

print ("Random Normal Array Mean Centered", x[0:10])


print("mean",np.mean(x))

plt.hist(x)
plt.show()

print("I am a champion of science!")


