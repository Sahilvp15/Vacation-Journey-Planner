# Vacation-Journey-Planner - Sahil Patel

### Project Goals

The Vacation Journey Planner application aims to provide an efficient and interactive tool for users to plan their journeys between different cities. Utilizing Dijkstra's algorithm, the application calculates the shortest path and suggests key attractions or 'happy spots' within destination cities, enhancing travel experiences by incorporating personalized recommendations.

### Significance of the Project

This application uniquely blends route optimization with personalized travel recommendations, elevating it from a simple journey planner to an engaging travel guide. By suggesting 'happy spots' within cities, the application fosters a joyful and connected travel experience, significantly enhancing user satisfaction.

### Installation and Usage Instructions

1. **Installation**: Requires any Python-supportive IDE with Tkinter. Tkinter typically comes pre-installed with Python, simplifying setup.

2. **Usage**: Users select start and destination cities from drop-down menus. Clicking "Find Path" reveals the shortest route, total distance, intermediate stops, and recommended attractions.

### Code Structure

The program uses a `CityGraph` class to manage the graph data structure, handling city additions and connections. It implements Dijkstra's algorithm within the `calculate_shortest_distances` method, calculating shortest paths between cities.

- **Tkinter GUI**: Sets up the user interface, allowing city selection and displaying results.
- **Main Loop**: The event loop is initiated with `window.mainloop()`.

### Dijkstra's Algorithm Explanation

Dijkstra's algorithm is used here in the `calculate_shortest_distances` method to find the shortest path between two cities. The steps are as follows:

**Initialization:** 
    - A priority queue (`priority_queue`) is used to efficiently retrieve the next city with the shortest known distance.
    - A dictionary (`distances`) tracks the shortest known distance to each city, initialized to infinity for all cities except the start city (set to 0).
    - Another dictionary (`previous_city`) tracks the previous city on the shortest path to each city.

**Algorithm Loop:** 
    - The city with the smallest known distance is popped from the priority queue.
    - If this city is the destination, the algorithm stops.
    - Otherwise, for each neighboring city, if the distance through the current city is shorter than the known distance, update the distance and add the neighbor to the priority queue.

**Path Reconstruction:**
    - Once the destination is reached or determined to be unreachable, the path is reconstructed in reverse using the `previous_city` dictionary.
    - The path and the total distance are returned.

Dijkstra's algorithm is very efficient and works well for applications like finding the shortest path in a network of cities. 

### Functionalities and Test Results

- **Accurate Path Calculation**: Confirms the shortest paths using Dijkstra's algorithm.
- **Responsive UI**: Users interact through a simple GUI, selecting cities and viewing results.
- **Attraction Recommendations**: Enhances travel planning by suggesting places to visit.

Test results demonstrate accurate path calculations and responsive UI elements.
First picture demonstrates the interative GUI where users can use the dropdown feature to selection the starting city and the destination city.

<img width="606" alt="Screenshot 2023-11-22 at 12 58 07 PM" src="https://github.com/Kunj-13/Vacation-Journey-Planner/assets/143433713/2d40fefc-aefb-4c96-9005-834a514d57ff">

The picture below shows the results that users achieve after selecting the starting and destination cities. In this example, it shows the user selected Los Angeles as starting city and New York as destination city. After that, the application shows the users the shortest route in this case it was Los Angeles to Chicago to New York while showing the total miles distance after calculation. Also, it displays famous spots to visit in New York which are Times Square and Central Park. 

<img width="608" alt="Screenshot 2023-11-22 at 12 58 33 PM" src="https://github.com/Kunj-13/Vacation-Journey-Planner/assets/143433713/8918dbed-b933-43d0-a755-3a14cae6a3b2">

### Discussion and Conclusions

The project successfully meets its objectives by providing efficient travel planning and enhancing user happiness through travel recommendations. However, it faces some limitations like the static city and connection data, and the absence of real-time traffic or weather conditions. For instance, users are only provided limited selections of cities, however, it is still very valuable application that can help tremendously in planning trips. The learnings from the course were effectively applied in implementing the Dijkstra algorithm and creating a user-friendly GUI. Future enhancements could include dynamic data updates and integration with real-time travel APIs.
