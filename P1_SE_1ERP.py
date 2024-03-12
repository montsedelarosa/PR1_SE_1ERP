from collections import defaultdict, deque

class CityMap: #Representa el mapa de ciudades, la clase utiliza un diccionario defaultdict (self.graph) para almacenar las conexiones entre las ciudades.
    def __init__(self):
        self.graph = defaultdict(list)

    def add_connection(self, city1, city2): #Permite agregar una conexión entre dos ciudades al mapa. Agrega la conexión entre city1 y city2 tanto desde city1 como desde city2 en el diccionario self.graph.
        self.graph[city1].append(city2)
        self.graph[city2].append(city1)

    def is_connected(self, start_city, end_city): #Utiliza el algoritmo de búsqueda en anchura (BFS) para verificar si hay un camino entre dos ciudades dadas. 
        visited = set()
        queue = deque()

        queue.append(start_city)
        visited.add(start_city)

        while queue: #Explora las ciudades vecinas de la ciudad actual (sacada de la cola queue).
            current_city = queue.popleft()
            if current_city == end_city:
                return True

            for neighbor_city in self.graph[current_city]:
                if neighbor_city not in visited:
                    queue.append(neighbor_city)
                    visited.add(neighbor_city)

        return False

# Crear un mapa de ciudades de ejemplo
city_map = CityMap()
city_map.add_connection("New York", "Boston")
city_map.add_connection("Boston", "Chicago")
city_map.add_connection("Chicago", "Los Angeles")
city_map.add_connection("Los Angeles", "San Francisco")

start_city = "San Francisco"
end_city = "Los Angeles"

if city_map.is_connected(start_city, end_city):
    print(f"Hay un camino entre {start_city} y {end_city}.")
else:
    print(f"No hay camino entre {start_city} y {end_city}.")
