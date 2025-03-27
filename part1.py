import numpy as np

data = np.loadtxt('Case2data.csv', delimiter=',', skiprows=1)

def get_q_with_eoq(lam,k,c,h):
    q = (2*k*lam)/(h*c)
    q = np.sqrt(q)
    return q

def run_strategy1(data):

    current_inventory = 0
    current_cost = 0

    for i in range(len(data)-1):

        if current_inventory <= 0: # se usa sin el -1 en el for
        # if current_inventory - data[i+1, 1] <= 0:

            lam = data[i,1]
            k = data[i,2]
            c = data[i,3]
            h = data[i,4]
            q = get_q_with_eoq(lam,k,c,h)
            q = np.ceil(q) # para aproximar hacia arriba
            current_inventory = current_inventory + q
            current_cost = current_cost + k + c*q
        current_inventory = current_inventory - lam

        current_cost = current_cost + h*current_inventory
        print(i, current_inventory)

    return(current_cost)


final_cost = run_strategy1(data)

# preguntas:

# ordenes discretas?
# puedo tener inventario negativo?
