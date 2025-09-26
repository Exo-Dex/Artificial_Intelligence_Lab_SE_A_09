def dfs(maze, start, end):
	stack = [start] # Initialize stack with start position
	visited = set() # Track visited positions
	parent = {start: None}  # Store parent to reconstruct path

	while stack:
		position = stack.pop() # Get current position
		x, y = position

        # Check if we've reached the end
		if position == end:
			path = []
			while position is not None:
				path.append(position)
				position = parent[position]
			path.reverse()
			return path  # Return the path as a list of coordinates

        # Mark the current cell as visited
		visited.add((x, y))

        # Explore neighbors (up, down, left, right)
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			new_x, new_y = x + dx, y + dy

            # Check bounds and if the cell is already visited or is a wall
			if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
					maze[new_x][new_y] == 0 and (new_x, new_y) not in visited):
				stack.append((new_x, new_y))
				parent[(new_x, new_y)] = position
				
	return False # Return False if no path is found

# Example maze: 0 -> open path, 1 -> wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Start and end positions
start = (0, 0)
end = (4, 4)

# Solve the maze
def main():
    path = dfs(maze, start, end)
    if path:
        print("Path found!")
        print("Path:", path)
        print("Length:", len(path) - 1)  # steps taken
    else:
        print("No path exists.")

main()
