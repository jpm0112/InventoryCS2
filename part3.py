import pyomo.environ as pyo

# Example data (you can replace with your actual data)
T = 7
d = {1: 15, 2: 14, 3: 13, 4: 10, 5: 8, 6: 6, 7: 5}
K = {1: 40, 2: 45, 3: 48.66, 4: 50, 5: 48.66, 6: 45, 7: 40}
c = {1: 4.75, 2: 4, 3: 3.25, 4: 2.7, 5: 2.5, 6: 2, 7: 2}
h = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}

# Large M (for q_t <= δ_t·M)
M = sum(d.values())  # or a suitably large number
x0 = 0  # initial inventory

model = pyo.ConcreteModel()

# Sets
model.t = pyo.RangeSet(1, T)

# Decision variables
model.x = pyo.Var(range(T + 2), domain=pyo.NonNegativeReals)  # x[0..T+1]
model.q = pyo.Var(model.t, domain=pyo.NonNegativeReals)
model.delta = pyo.Var(model.t, domain=pyo.Binary)

# Fix initial inventory
model.x[0].fix(x0)


# Inventory balance: x[t+1] = x[t] + q[t] - d[t]
def inventory_rule(m, t):
    return m.x[t + 1] == m.x[t] + m.q[t] - d[t]


model.InventoryConstraint = pyo.Constraint(model.t, rule=inventory_rule)


# Big-M constraint: q[t] <= δ[t]*M
def bigM_rule(m, t):
    return m.q[t] <= m.delta[t] * M


model.BigMConstraint = pyo.Constraint(model.t, rule=bigM_rule)


# Objective: minimize sum of setup, purchasing, and holding costs
def obj_rule(m):
    return sum(K[t] * m.delta[t] + c[t] * m.q[t] + h[t] * m.x[t + 1] for t in m.t)


model.Obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

# Solve
solver = pyo.SolverFactory('glpk')
solver.solve(model)

# Results
print("Order quantities q[t]:")
for t in model.t:
    print(f"Period {t}: {model.q[t].value:.2f}")
print("\nInventory levels x[t]:")
for t in range(T + 2):
    print(f"x[{t}]: {model.x[t].value:.2f}")
