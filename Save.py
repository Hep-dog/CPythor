import numpy as np

data_read = np.loadtxt('data/Test.csv', delimiter=',')
n_dim = data_read.shape[0]

a = []
for i in range(n_dim):
    a.append(-1.0)

b = np.array(a)
b = b.reshape(n_dim,1)

data_new = np.column_stack((data_read, b))
print(data_read.shape, "    ", n_dim, "     ", data_new.shape)

np.savetxt("data/New.csv", data_new, delimiter=",", fmt="%s")


