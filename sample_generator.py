import numpy as np
import os
import csv

def generate_distance_matrix(N):
    distances = np.random.randint(1, 100, size=(N, N))
    distances = (distances + distances.T) // 2
    np.fill_diagonal(distances, 0)
    return distances

def store_matrix_csv(matrix, folder, file_name):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    file_path = os.path.join(folder, file_name)
    
    with open(file_path, 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(matrix)

    print(f"Matrix stored in {file_path}")

N = int(input("Type the size of the sample N: "))
tarjet_folder = f"sample{N}"

for i in range(20):
    distance_matrix = generate_distance_matrix(N)
    file_name = f"distance_matrix_{i}.csv"
    store_matrix_csv(distance_matrix, tarjet_folder, file_name)
