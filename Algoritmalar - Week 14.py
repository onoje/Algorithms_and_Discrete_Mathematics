import heapq

def dijkstra(graph, source):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3},
    'D': {}
}

source_vertex = 'A'
distances_from_source = dijkstra(graph, source_vertex)
print(f"Shortest paths from {source_vertex}: {distances_from_source}")
def shortest_path_between(graph, source, target):
    distances = dijkstra(graph, source)
    return distances.get(target, float('infinity'))

start = 'A'
end = 'D'
shortest_distance = shortest_path_between(graph, start, end)
print(f"Shortest path from {start} to {end}: {shortest_distance}")