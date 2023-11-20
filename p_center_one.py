import numpy as np

def p_center_heuristic(distance_matrix, p, n_clients, n_facilities):
    selected_facilities = []
    assignment = [0]*n_clients

    for _ in range(p):
        max_distance = -1
        for i in range(n_clients):
            for j in range(n_facilities):
                if j not in selected_facilities and distance_matrix[i][j] > max_distance:
                    max_distance = distance_matrix[i][j]
                    max_j = j
        selected_facilities.append(max_j)

        print(f"\nIteration {_ + 1}:")
        print(f"Selected Facilities: {selected_facilities}")

    for i in range(n_clients):
        min_distance = float('inf')
        for j in selected_facilities:
            if distance_matrix[i][j] < min_distance:
                min_distance = distance_matrix[i][j]
                min_j = j
        assignment[i] = min_j

    final_distance = max(np.min(distance_matrix[:, selected_facilities], axis=1))

    return selected_facilities, assignment, final_distance

distance_matrix = np.loadtxt('./sample10/distance_matrix_0.csv', delimiter=',')
p = 2
n_clients = 10
n_facilities = 5
selected_facilities, assignment, final_distance = p_center_heuristic(distance_matrix, p, n_clients, n_facilities)

print(f"\nNumber of possible facilities: {n_facilities}, p: {p}")
print(f"Selected Facilities: {selected_facilities}")
print(f"Client Assignment: {assignment}")
print(f"Final Maximum Distance: {final_distance}")
