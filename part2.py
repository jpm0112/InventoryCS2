import numpy as np

data = np.loadtxt('Case2data.csv', delimiter=',', skiprows=1)


# def calculate_average_cost(data, s, t, ctt_matrix):
#
#     lam = data[s,1]
#     k = data[s,2]
#     c = data[s,3]
#     h = data[s,4]
#
#     if ctt_matrix[s,t] != 0:
#         return ctt_matrix[s, t]
#
#     value = 0
#     for i in range(t-s):
#         for j in range(t-i):
#             value = value + data[j,1]
#
#     value = value * h
#     value = value + k
#     value = value /(t-s+1)
#
#
#     # add purchasing cost:
#     purchasing_cost = 0
#     for i in range(t-s):
#         purchasing_cost = purchasing_cost + data[i,1]*c
#     value = value + purchasing_cost
#
#     return value


def calculate_average_cost(data, s, t, ctt_matrix):
    K = data[s, 2]  # setup cost
    c = data[s, 3]  # purchasing cost
    h = data[s, 4]  # holding cost

    if ctt_matrix[s, t] != 0:
        return ctt_matrix[s, t]

    # Sum total demand from period s to t (inclusive)
    total_demand = np.sum(data[s:t + 1, 1])

    # Holding cost: for periods s+1 to t, holding cost is multiplied by the number of periods inventory is held.
    holding_cost = sum(h * (i - s) * data[i, 1] for i in range(s + 1, t + 1))

    avg_cost = (K + holding_cost + c * total_demand) / (t - s + 1)




    return avg_cost

s = 0
t = 1

q_list = np.zeros(len(data))
q_list[s] = data[0,1]
ctt_matrix = np.zeros([len(data), len(data)])
ctt_matrix[0,0] = data[0,2]

for t in range(len(data)):

    if calculate_average_cost(data, s, t, ctt_matrix) < calculate_average_cost(data, s, t - 1, ctt_matrix):
        q_list[s] = q_list[s] + data[t, 1]
    else:
        s = t
        q_list[t] = data[t, 1]
        ctt_matrix[t,t] = data[s,2]


print(q_list)

purchase_cost = 0
for i in range(len(q_list)):
    purchase_cost =purchase_cost + q_list[s]*data[i,1]

print(purchase_cost)














