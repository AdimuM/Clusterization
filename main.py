import numpy as np

def calculate_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

def find_cluster_center(cluster):
    return np.mean(cluster)

def forel_clustering(data, radius):
    clusters = []
    visited = [False] * len(data)

    for idx, point in enumerate(data):
        if visited[idx]:
            continue

        cluster = []
        cluster.append(point)
        visited[idx] = True

        center = find_cluster_center(cluster)

        while True:
            new_cluster = []
            for idx, point in enumerate(data):
                if visited[idx]:
                    continue

                distance = calculate_distance(center, point)
                if distance <= radius:
                    new_cluster.append(point)
                    visited[idx] = True

            new_center = find_cluster_center(new_cluster)
            if np.array_equal(center, new_center):
                break

            cluster = new_cluster
            center = new_center

        clusters.append(cluster)

    return clusters

# Example 
data = [[1, 2], [2, 1], [5, 6], [6, 5], [8, 9], [9, 8]]
radius = 2

clusters = forel_clustering(data, radius)

for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}:")
    for point in cluster:
        print(point)
    
    
