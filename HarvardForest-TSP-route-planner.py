# Define a function to convert a four digit number to a pair of coordinates
def num2coord(num):
    # Convert the number to a string
    num_str = str(num)
    # Check if the number has four digits
    if len(num_str) == 4:
        # Extract the first two digits as the x coordinate
        x = int(num_str[:2])
        # Extract the last two digits as the y coordinate
        y = int(num_str[2:])
        # Return the pair of coordinates as a tuple
        return (x, y)
    else:
        # If the number does not have four digits, print an error message and return None
        print("Invalid number: must have four digits")
        return None

# Define a function to convert a list of four digit numbers to a list of coordinates
def nums2coords(nums):
    # Initialize an empty list to store the coordinates
    coords = []
    # Loop through each number in the list
    for num in nums:
        # Convert the number to a pair of coordinates using num2coord function
        coord = num2coord(num)
        # Check if the conversion was successful
        if coord is not None:
            # Append the coordinate to the coords list
            coords.append(coord)
        else:
            # If the conversion failed, print an error message and return None
            print("Conversion failed: invalid input")
            return None
    # Return the coords list
    return coords

# Import math library for square root function
import math

# Define a function to calculate the Euclidean distance between two points
def distance(p1, p2):
    # Get the x and y coordinates of each point
    x1, y1 = p1
    x2, y2 = p2
    # Calculate the squared difference of x and y coordinates
    dx = (x1 - x2) ** 2
    dy = (y1 - y2) ** 2
    # Calculate and return the square root of the sum of squared differences
    return math.sqrt(dx + dy)

# Define a function to find the closest point among a list of points given a reference point
def closest_point(ref_point, points):
    # Initialize a variable to store the minimum distance as infinity
    min_dist = math.inf
    # Initialize a variable to store the closest point as None
    closest_point = None
    # Loop through each point in the list
    for point in points:
        # Calculate the distance between the reference point and the current point using distance function
        dist = distance(ref_point, point)
        # Check if the distance is smaller than the minimum distance
        if dist < min_dist:
            # Update the minimum distance and the closest point accordingly
            min_dist = dist
            closest_point = point
    # Return the closest point and its distance from the reference point as a tuple
    return (closest_point, min_dist)

# Define a function to check if a point is already visited given a list of visited points
def is_visited(point, visited):
    # Check if the point is in the visited list
    if point in visited:
        # Return True if yes
        return True
    else:
        # Return False if no
        return False

# Define a function to find the shortest path using nearest neighbor algorithm
def nearest_neighbor(coords):
    # Check if the coords list is empty
    if not coords:
        # If yes, print an error message and return None
        print("No coordinates given")
        return None
    # Initialize a variable to store the current point as the first point in the coords list
    current_point = coords[0]
    # Initialize a list to store the visited points as empty
    visited = []
    # Initialize a list to store the path as empty
    path = []
    # Initialize a variable to store the total distance as zero
    total_distance = 0
    # Loop until all points are visited
    while len(visited) < len(coords):
        # Append the current point to the path list
        path.append(current_point)
        # Append the current point to the visited list
        visited.append(current_point)
        # Find the closest point among the coords list that is not already visited using closest_point and is_visited functions
        closest, dist = closest_point(current_point, [p for p in coords if not is_visited(p, visited)])
        # Check if there is a closest point found
        if closest is not None:
            # If yes, update the current point as the closest point
            current_point = closest
            # Update the total distance by adding the distance to the closest point
            total_distance += dist
        else:
            # If no, it means all points are visited, so break out of the loop
            break
    # Return the path list and the total distance as a tuple
    return (path, total_distance)

nums = [1420, 3120, 2308, 1717, 3119, 2113, 1814, 1518, 2517, 1115]

coords = nums2coords(nums)
print(coords)

path, distance_traveled = nearest_neighbor(coords)
print(path)
print(distance)

# Import matplotlib.pyplot library for plotting
import matplotlib.pyplot as plt

# Define a function to graph the points and line segments
def graph_path(path, distance):
    # Check if the path list is empty
    if not path:
        # If yes, print an error message and return None
        print("No path given")
        return None
    # Initialize two lists to store the x and y coordinates of the points
    x = []
    y = []
    # Loop through each point in the path list
    for point in path:
        # Get the x and y coordinates of each point
        x_coord, y_coord = point
        # Append them to the x and y lists respectively
        x.append(x_coord)
        y.append(y_coord)
    # Plot the points as scatter plot using plt.scatter function
    plt.scatter(x, y, color='blue', label='Points')
    # Plot the line segments as line plot using plt.plot function
    plt.plot(x, y, color='red', label='Shortest path')
    # Add a title to the plot using plt.title function
    plt.title(f"Shortest path with distance {distance}")
    # Add a legend to the plot using plt.legend function
    plt.legend()
    # Show the plot using plt.show function
    plt.show()

coords = nums2coords(nums)
print(coords)

path, distance = nearest_neighbor(coords)
print(path)
print(distance)

graph_path(path, distance)
