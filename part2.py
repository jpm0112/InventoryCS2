import numpy as np

data = np.loadtxt('Case2data.csv', delimiter=',', skiprows=1)


def calculate_average_cost(data, s):

    lam = data[s,1]
    k = data[s,2]
    c = data[s,3]
    h = data[s,4]

    t = len(data)
    value = 0
    for i in range(t-s):
        for j in range(t-i):
            value = value + data[j,1]

    value = value * h

    value = value + k

    value = value /(t-s+1)


    # add purchasing cost:

    purchasing_cost = 0
    for i in range(t-s):
        purchasing_cost = purchasing_cost + data[i,1]*c

    value = value + purchasing_cost


    return (value)



s = 1
t = 2

qs = data[0,1]
q1 = data[0,1]
c11 = k

for t in range(1,len(data)):
    avg_c = calculate_average_cost(data, s)
