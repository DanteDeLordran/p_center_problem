import numpy as np
import time
from colorama import Fore, Style

def p_center_heuristic(distance_matrix, p, n_clients, n_facilities):
    start_time = time.time()
    selected_facilities = []
    not_selected_facilities = list(range(n_facilities))  # Initially, all facilities are not selected
    assignment = [-1]*n_clients

    for iteration in range(p):
        max_distance = -1
        for i in range(n_clients):
            for j in not_selected_facilities:
                if distance_matrix[i][j] > max_distance:
                    max_distance = distance_matrix[i][j]
                    max_j = j

        selected_facilities.append(max_j)
        not_selected_facilities.remove(max_j)

        print(f"\nIteration {iteration + 1}:")
        print(f"Selected Facilities: {selected_facilities}")
        print(f"Not Selected Facilities: {not_selected_facilities}")

        # Print distances for each client to the selected facilities in this iteration
        distances_to_selected = distance_matrix[:, selected_facilities]
        print(f"Distances to Selected Facilities:\n{distances_to_selected}")

        # Assign clients to the closest selected facility
        for i in range(n_clients):
            min_distance = float('inf')
            for j in selected_facilities:
                if distance_matrix[i][j] < min_distance:
                    min_distance = distance_matrix[i][j]
                    min_j = j
            assignment[i] = (i, min_j)

        print(f"Client Assignment: {assignment}")

    final_distance = max(np.min(distance_matrix[:, selected_facilities], axis=1))

    end_time = time.time()  # Record the end time
    processing_time = end_time - start_time  # Calculate the processing time

    return selected_facilities, not_selected_facilities, assignment, final_distance, processing_time

def print_colored(message, color=Fore.WHITE, style=Style.NORMAL):
    print(f"{style}{color}{message}{Style.RESET_ALL}")

instance = int(input("Instance to run : "))
distance_matrix = np.loadtxt(f'./sample10/distance_matrix_{instance}.csv', delimiter=',')
p = 3
n_clients = 5
n_facilities = 5
selected_facilities, not_selected_facilities, assignment, final_distance, processing_time = p_center_heuristic(distance_matrix, p, n_clients, n_facilities)

print_colored("\n\n-------Final report--------", Fore.YELLOW, Style.BRIGHT)
print_colored(f"Number of possible facilities: {n_facilities}, p: {p}", Fore.CYAN)
print_colored(f"Selected Facilities: {selected_facilities}", Fore.GREEN)
print_colored(f"Not selected Facilities: {not_selected_facilities}", Fore.RED)
print_colored(f"Client Assignment: {assignment}", Fore.MAGENTA)
print_colored(f"Final Maximum Distance: {final_distance}", Fore.CYAN)
print_colored(f"Processing Time: {processing_time:.10f} seconds", Fore.WHITE)
