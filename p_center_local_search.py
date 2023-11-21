import numpy as np
import time
from p_center_heuristic import p_center_heuristic
from colorama import Fore, Style

def local_search(distance_matrix, selected_facilities, not_selected_facilities, assignment, final_distance):
    start_time = time.time()

    improved = True
    while improved:
        improved = False
        for selected_index, selected_facility in enumerate(selected_facilities):
            for not_selected_facility in not_selected_facilities:
                # Swap selected and not selected facilities
                new_selected_facilities = list(selected_facilities)
                new_selected_facilities[selected_index] = not_selected_facility

                # Calculate the new final distance
                new_final_distance = max(np.min(distance_matrix[:, new_selected_facilities], axis=1))

                # Check if the new solution is better
                if new_final_distance < final_distance:
                    selected_facilities = new_selected_facilities
                    final_distance = new_final_distance
                    improved = True

    end_time = time.time()
    processing_time = end_time - start_time

    return selected_facilities, not_selected_facilities, assignment, final_distance, processing_time

def print_colored(message, color=Fore.WHITE, style=Style.NORMAL):
    print(f"{style}{color}{message}{Style.RESET_ALL}")

instance = int(input("Instance to run : "))
distance_matrix = np.loadtxt(f'./sample10/distance_matrix_{instance}.csv', delimiter=',')
p = 3
n_clients = 5
n_facilities = 5
selected_facilities, not_selected_facilities, assignment, final_distance, processing_time = p_center_heuristic(distance_matrix, p, n_clients, n_facilities)

# Perform local search
selected_facilities, not_selected_facilities, assignment, final_distance, processing_time_ls = local_search(
    distance_matrix, selected_facilities, not_selected_facilities, assignment, final_distance
)

# Print the updated final report with local search
print_colored("\n\n-------Final report with Local Search--------", Fore.YELLOW, Style.BRIGHT)
print_colored(f"Selected Facilities: {selected_facilities}", Fore.GREEN)
print_colored(f"Not selected Facilities: {not_selected_facilities}", Fore.RED)
print_colored(f"Client Assignment: {assignment}", Fore.CYAN)
print_colored(f"Final Maximum Distance: {final_distance}", Fore.MAGENTA)
print_colored(f"Processing Time: {processing_time + processing_time_ls:.10f} seconds", Fore.WHITE)
