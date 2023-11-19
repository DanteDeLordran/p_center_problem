import pulp
import numpy as np

distances = np.loadtxt('./samples5/distance_matrix_0.csv', delimiter=',')

problem = pulp.LpProblem("p-center", pulp.LpMinimize)

n_clients, n_facilities = distances.shape
p = 3

x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n_clients) for j in range(n_facilities)), cat='Binary')
y = pulp.LpVariable.dicts("y", (i for i in range(n_facilities)), cat='Binary')
z = pulp.LpVariable("z", lowBound=0)

problem += z, "Minimize the maximum distance"

for i in range(n_clients):
    problem += pulp.lpSum(x[i, j] for j in range(n_facilities)) == 1

for i in range(n_clients):
    for j in range(n_facilities):
        problem += z >= distances[i, j] * x[i, j]

for j in range(n_facilities):
    problem += pulp.lpSum(x[i, j] for i in range(n_clients)) <= n_clients * y[j]

problem += pulp.lpSum(y[j] for j in range(n_facilities)) == p

problem.solve()

print("Status:", pulp.LpStatus[problem.status])
for v in problem.variables():
    print(v.name, "=", v.varValue)
print("Objective =", pulp.value(problem.objective))
