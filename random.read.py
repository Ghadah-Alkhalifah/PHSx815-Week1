import numpy as np
import matplotlib.pyplot as plt

# Load random number from txt file
filex='Random.txt'
data=np.loadtxt(filex)


# create histogram of data 
n, bins, patches = plt.hist(data, 40, density=True, color='skyblue', alpha=0.75, rwidth=.9, ec='black')

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)
plt.style.use('ggplot')
plt.savefig('plot.pdf')

# show figure (program only ends once closed)
plt.show()
