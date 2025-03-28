import numpy as np


def compute_cost(data, s, t):
    # data columns: [t, d(t), K(t), c(t), h(t)]
    K_s = data[s, 2]  # setup cost in period s
    c_s = data[s, 3]  # purchasing cost in period s

    # Sum of demands from s..t
    demand_sum = np.sum(data[s:t + 1, 1])

    # Purchasing cost
    purchase_cost = demand_sum * c_s

    # Holding cost: hold period k's demand for each period from k+1..t
    holding_cost = 0
    for k in range(s, t):
        for u in range(k + 1, t + 1):
            holding_cost += data[k, 1] * data[u, 4]

    return K_s + purchase_cost + holding_cost


def silver_meal(data):
    N = len(data)
    order_plan = np.zeros(N)
    s = 0
    while s < N:
        best_avg = float('inf')
        best_t = s
        for t in range(s, N):
            cost = compute_cost(data, s, t)
            avg_cost = cost / (t - s + 1)
            if avg_cost <= best_avg:
                best_avg = avg_cost
                best_t = t
            else:
                break
        # Place one order covering periods s..best_t
        for k in range(s, best_t + 1):
            order_plan[k] = data[k, 1]
        s = best_t + 1
    return order_plan

# Example usage:
data = np.loadtxt('Case2data.csv', delimiter=',', skiprows=1)
plan = silver_meal(data)
print(plan)





import matplotlib.pyplot as plt


def plot_order_plan(data, order_plan):
    # data[:,0] holds the period numbers
    periods = data[:, 0]
    plt.bar(periods, order_plan)
    plt.xlabel("Period")
    plt.ylabel("Order Quantity")
    plt.title("Silver-Meal Order Plan")
    plt.show()

plan = silver_meal(data)
plot_order_plan(data, plan)
plot_order_plan(data, q_list)