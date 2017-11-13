from matplotlib import pyplot as plt
import numpy as np

data = np.genfromtxt('people.csv', delimiter=',', skip_header=10,
                     skip_footer=10)

plt.plot(data['reviewerID'],data['overall'])

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()