import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []
    
    def add_connection(self, loc1, loc2, distance):
        if loc1 in self.graph and loc2 in self.graph:
            self.graph[loc1].append((distance, loc2))
            self.graph[loc2].append((distance, loc1))
        else:
            raise ValueError("Both locations must be added first.")
    
    def dijkstra(self, start, end):
        heap = [(0, start)]
        distances = {location: float('inf') for location in self.graph}
        distances[start] = 0
        while heap:
            (current_distance, current_location) = heapq.heappop(heap)
            if current_location == end:
                return current_distance
            if current_distance > distances[current_location]:
                continue
            for neighbor_distance, neighbor in self.graph[current_location]:
                distance = current_distance + neighbor_distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        return float('inf')
    
    def view_connections(self):
        for location, connections in self.graph.items():
            print(f"{location}: {', '.join([f'{dist} to {loc}' for dist, loc in connections])}")

planner = Graph()
planner.add_location("A")
planner.add_location("B")
planner.add_location("C")
planner.add_connection("A", "B", 10)
planner.add_connection("B", "C", 20)
planner.add_connection("A", "C", 15)

print("Connections:")
planner.view_connections()

print("\nShortest path from A to C:")
print(planner.dijkstra("A", "C"))
