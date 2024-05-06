import tkinter as tk
from tkinter import ttk
import heapq
from collections import defaultdict

class CityGraph:
    def __init__(self):
        # Initialize the graph with sets and dictionaries to store cities and connections
        self.cities = set()
        self.connections = defaultdict(list)

    def add_city(self, name):
        self.cities.add(name)

    def connect_cities(self, city_a, city_b, distance):
        self.connections[city_a].append((city_b, distance))
        self.connections[city_b].append((city_a, distance))

    # Calculate the shortest distance between two cities using Dijkstra's algorithm
    def calculate_shortest_distances(self, start, end):
        if start not in self.cities or end not in self.cities:
            return float('inf'), []

        # Initialize distances and set up priority queue
        distances = {city: float('inf') for city in self.cities}
        distances[start] = 0
        priority_queue = [(0, start)]
        previous_city = {city: None for city in self.cities}

        while priority_queue:
            # Pop the city with the shortest distance from the queue
            current_distance, current_city = heapq.heappop(priority_queue)

            # Break if the end city is reached
            if current_city == end:
                break

            # Update distances for neighboring cities
            for neighbor, neighbor_distance in self.connections[current_city]:
                distance = current_distance + neighbor_distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_city[neighbor] = current_city
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Construct the path from start to end
        path = []
        current = end
        if distances[current] == float('inf'):
            return float('inf'), path  # No path found

        while current is not None:
            path.append(current)
            current = previous_city[current]
        path.reverse()

        return distances[end], path

# Function to handle finding path and updating the GUI
def find_path():
    starting_city = start_city_var.get()
    ending_city = end_city_var.get()
    total_distance, path = city_graph.calculate_shortest_distances(starting_city, ending_city)

    result_text = ""
    if total_distance == float('inf'):
        result_text = f"No path found from {starting_city} to {ending_city}.\n"
    else:
        result_text = (f"Journey from {starting_city} to {ending_city}\n" +
                       "-" * 40 + "\n" +
                       f"Shortest path: {' -> '.join(path)}\n" +
                       f"Total distance: {total_distance} miles\n\n")

        result_text += "Cities you will visit:\n"
        for city in path:
            result_text += f"  - {city}\n"

        result_text += "\nHot Spots to visit in each city:\n"
        for city in path:
            if city in Hot_spots:
                result_text += f"{city}:\n"
                for spot in Hot_spots[city]:
                    result_text += f"  - {spot}\n"
            else:
                result_text += f"{city}: No Hot spots listed for this city.\n"
            result_text += "\n"

        result_text += "-" * 40

    result_label.config(text=result_text, font=("Arial", 12))

# Create Tkinter window
window = tk.Tk()
window.title("Vacation Journey Planner")

# Create a style for the GUI
style = ttk.Style()
style.theme_use('default')
style.configure('TCombobox', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 12))

# Create and set up city graph
city_graph = CityGraph()
cities = ["New York", "San Francisco", "Los Angeles", "Chicago",
          "Seattle", "Miami", "Denver", "Boston", "Austin", "Washington D.C.", "Las Vegas", "Honolulu",
          "Portland", "Phoenix", "Atlanta", "New Orleans"]
for city in cities:
    city_graph.add_city(city)

# Connect cities
city_graph.connect_cities("New York", "San Francisco", 3000)
city_graph.connect_cities("New York", "Chicago", 1000)
city_graph.connect_cities("Los Angeles", "San Francisco", 500)
city_graph.connect_cities("Los Angeles", "Chicago", 2000)
city_graph.connect_cities("New York", "Seattle", 2500)
city_graph.connect_cities("San Francisco", "Miami", 3500)
city_graph.connect_cities("New York", "Washington D.C.", 225)
city_graph.connect_cities("Washington D.C.", "Chicago", 700)
city_graph.connect_cities("Los Angeles", "Las Vegas", 270)
city_graph.connect_cities("San Francisco", "Honolulu", 2400)
city_graph.connect_cities("Seattle", "Portland", 175)
city_graph.connect_cities("Los Angeles", "Phoenix", 370)
city_graph.connect_cities("Miami", "Atlanta", 660)
city_graph.connect_cities("New Orleans", "Atlanta", 470)

# Define Hot spots for each city
Hot_spots = {
    "New York": ["Central Park", "Times Square", "9/11 Memorial", "The Metropolitan Museum of Art"],
    "San Francisco": ["Golden Gate Park", "Fisherman's Wharf", "Alcatraz Island", "Exploratorium"],
    "Los Angeles": ["Griffith Observatory", "Santa Monica Pier", "Hollywood Walk of Fame", "Universal Studios Hollywood"],
    "Chicago": ["Millennium Park", "Navy Pier", "The Art Institute of Chicago", "Skydeck Chicago"],
    "Seattle": ["Space Needle", "Pike Place Market", "Chihuly Garden and Glass", "Museum of Pop Culture"],
    "Miami": ["South Beach", "Art Deco Historic District", "Vizcaya Museum & Gardens", "Everglades National Park"],
    "Denver": ["Red Rocks Park", "Denver Zoo", "Denver Botanic Gardens", "Denver Art Museum"],
    "Boston": ["Freedom Trail", "Harvard University", "Museum of Fine Arts", "New England Aquarium"],
    "Austin": ["Sixth Street", "Lady Bird Lake", "Barton Creek Greenbelt", "Texas State Capitol"],
    "Washington D.C.": ["National Mall", "Smithsonian Museums", "White House", "United States Holocaust Memorial Museum"],
    "Las Vegas": ["The Strip", "Bellagio Fountains", "Red Rock Canyon", "Neon Museum"],
    "Honolulu": ["Waikiki Beach", "Pearl Harbor", "Diamond Head", "Iolani Palace"],
    "Portland": ["Forest Park", "Powell's City of Books", "International Rose Test Garden", "Lan Su Chinese Garden"],
    "Phoenix": ["Papago Park", "Desert Botanical Garden", "Heard Museum", "Taliesin West"],
    "Atlanta": ["Georgia Aquarium", "World of Coca-Cola", "Martin Luther King Jr. National Historic Site", "Centennial Olympic Park"],
    "New Orleans": ["French Quarter", "National WWII Museum", "Jackson Square", "Garden District"]
}

# UI Elements
start_city_var = tk.StringVar()
end_city_var = tk.StringVar()

tk.Label(window, text="Starting City:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
start_city_entry = ttk.Combobox(window, textvariable=start_city_var, values=cities, font=("Arial", 12))
start_city_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Ending City:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
end_city_entry = ttk.Combobox(window, textvariable=end_city_var, values=cities, font=("Arial", 12))
end_city_entry.grid(row=1, column=1, padx=10, pady=10)

find_path_button = ttk.Button(window, text="Find Path", command=find_path)
find_path_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="", justify=tk.LEFT, font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()