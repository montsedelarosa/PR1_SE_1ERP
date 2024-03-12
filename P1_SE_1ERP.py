class CityDirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_connection(self, from_city, to_city):
        if from_city not in self.graph:
            self.graph[from_city] = set()
        self.graph[from_city].add(to_city)

    def is_connected(self, start_city, end_city):
        visited = set()
        stack = [start_city]
        visited.add(start_city)

        while stack:
            current_city = stack.pop()
            if current_city == end_city:
                return True

            for neighbor_city in self.graph.get(current_city, []):
                if neighbor_city not in visited:
                    stack.append(neighbor_city)
                    a=visited.add(neighbor_city)
                    print("a")

        return False

# Crear un mapa de ciudades de ejemplo
city_map = CityDirectedGraph()
city_map.add_connection("New York", "Boston")
city_map.add_connection("Boston", "Chicago")
city_map.add_connection("Chicago", "Los Angeles")
city_map.add_connection("Los Angeles", "San Francisco")

# Definir las ciudades de inicio y fin
start_city = "New York"
end_city = "San Francisco"

# Verificar si hay un camino entre las ciudades de inicio y fin
if city_map.is_connected(start_city, end_city):
    print(f"Hay un camino entre {start_city} y {end_city}.")
else:
    print(f"No hay camino entre {start_city} y {end_city}.")
