# Travel Planner Using Graph

## Overview

The Travel Planner Using Graph project is a Python application designed to manage and plan travel routes between locations using graph data structures. It allows users to add locations, create connections between them, and find the shortest path between two locations using Dijkstra's algorithm.

## Features

- **Add Locations**: Add new locations to the graph.
- **Add Connections**: Define bidirectional connections between locations with specified distances.
- **Find Shortest Path**: Calculate the shortest path between two locations using Dijkstra's algorithm.
- **View Connections**: Display all connections and their distances.

## Requirements

- Python 3.x
- No additional libraries required (uses built-in modules only)

## Installation

1. Clone this repository or download the `Travel_planner_using_Graph.py` file.

   ```bash
   git clone <repository-url>
2. Navigate to the project directory.
   cd <project-directory>
### Usage
Open Travel_planner_using_Graph.py in your Python environment.

You can modify the example usage section to add your own locations and connections.

Run the script to see the connections and shortest path output.
  python Travel_planner_using_Graph.py
## Example

Here is a basic usage example included in the script:

```python
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

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
Based on graph theory concepts and Dijkstra's algorithm.
