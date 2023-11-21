import numpy as np
import time

def objective_function(distance_matrix, assignment):
    return max(np.min(distance_matrix[:, assignment], axis=1))

def local_search(current_solution, distance_matrix, p, n_clients, n_facilities, max_iterations=100):
    start_time = time.process_time()
    
    selected_facilities, not_selected_facilities, assignment, final_distance, _ = current_solution

    for iteration in range(max_iterations):
        # Iterate through clients and try swapping their assignments
        for client in range(n_clients):
            for new_facility in not_selected_facilities:
                # Try swapping the assignment of the current client to a not selected facility
                new_assignment = assignment.copy()
                new_assignment[client] = (client, new_facility)
                
                # Evaluate the objective function for the new assignment
                new_distance = objective_function(distance_matrix, [f[1] for f in new_assignment])
                
                # If the new assignment improves the objective function, update the solution
                if new_distance < final_distance:
                    assignment = new_assignment
                    final_distance = new_distance
                    selected_facilities = [f[1] for f in assignment]

        # Update the selected and not selected facilities based on the new assignment
        selected_facilities = list(set([f[1] for f in assignment]))
        not_selected_facilities = [f for f in range(n_facilities) if f not in selected_facilities]

        print(f"\nIteration {iteration + 1}:")
        print(f"Selected Facilities: {selected_facilities}")
        print(f"Not Selected Facilities: {not_selected_facilities}")
        print(f"Client Assignment: {assignment}")
        print(f"Final Maximum Distance: {final_distance}")

    end_time = time.process_time()
    processing_time = end_time - start_time

    return selected_facilities, not_selected_facilities, assignment, final_distance, processing_time

# Example usage
distance_matrix = np.loadtxt('./sample10/distance_matrix_0.csv', delimiter=',')
current_solution = (
    [1, 0, 3],
    [2, 4],
    [(0, 0), (1, 1), (2, 0), (3, 3), (4, 0)],
    60.0,
    0.015625
)

new_solution = local_search(current_solution, distance_matrix, p=3, n_clients=5, n_facilities=5)
print(new_solution)