# Manhattan Distance Heuristic
def heuristic(state, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            h += abs(i - x) + abs(j - y)
    return h

# Find position of 0
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors
def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Convert state to string for comparison
def state_to_str(state):
    return ''.join(str(cell) for row in state for cell in row)

# Print state with f(n)
def print_state(state, g, h):
    for row in state:
        print(['_' if val == 0 else val for val in row])
    print(f"g(n) = {g}, h(n) = {h}, f(n) = {g + h}")
    print("------")

# A* Algorithm
def a_star(start, goal):
    open_list = [[start, [], 0, heuristic(start, goal)]]  # [state, path, g, h]
    visited = []

    while open_list:
        current = min(open_list, key=lambda x: x[2] + x[3])
        open_list.remove(current)
        state, path, g, h = current

        if state == goal:
            return path + [[state, g, h]]

        visited.append(state_to_str(state))

        for neighbor in get_neighbors(state):
            if state_to_str(neighbor) in visited:
                continue
            new_g = g + 1
            new_h = heuristic(neighbor, goal)
            open_list.append([neighbor, path + [[state, g, h]], new_g, new_h])

    return None

# Input 3x3 state with '_' support
def input_state(prompt):
    print(prompt)
    state = []
    for i in range(3):
        while True:
            row_input = input(f"Enter row {i+1} (use _ for blank): ").strip().split()
            if len(row_input) != 3:
                print("❌ Enter exactly 3 values separated by spaces.")
                continue
            try:
                row = [0 if val == '_' else int(val) for val in row_input]
                state.append(row)
                break
            except ValueError:
                print("❌ Invalid input. Use digits or '_' for blank.")
    return state

# Main
start_state = input_state("Enter START state:")
goal_state = input_state("Enter GOAL state:")

solution = a_star(start_state, goal_state)

if solution:
    print("\nSteps to solve the puzzle (with f(n) = g(n) + h(n)):\n")
    for step in solution:
        state, g, h = step
        print_state(state, g, h)
else:
    print("No solution found.")
