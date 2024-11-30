import copy
import time
from visualize import visualize
from items import items_1
from itertools import permutations, product

# Define the Grid class
class Grid:
    def __init__(self, width=20, height=20):
        self.width = width  # Number of columns (x-axis)
        self.height = height  # Number of rows (y-axis)
        # Initialize grid cells to None (empty)
        self.cells = [[None for _ in range(self.width)] for _ in range(self.height)]

    def can_place(self, item, x, y):
        item_width, item_height = item.rotated_dimensions()
        # Check if item fits within grid boundaries
        if x + item_width > self.width or y + item_height > self.height:
            return False
        # Check for overlap with already placed items
        for i in range(y, y + item_height):
            for j in range(x, x + item_width):
                if self.cells[i][j] is not None:
                    return False
        return True

    def place_item(self, item, x, y):
        item_width, item_height = item.rotated_dimensions()
        for i in range(y, y + item_height):
            for j in range(x, x + item_width):
                self.cells[i][j] = item.item_id  # Mark cell with item's id

    def remove_item(self, item, x, y):
        item_width, item_height = item.rotated_dimensions()
        for i in range(y, y + item_height):
            for j in range(x, x + item_width):
                self.cells[i][j] = None  # Clear cell

    def copy(self):
        new_grid = Grid(self.width, self.height)
        new_grid.cells = [row[:] for row in self.cells] # Deep copy of own grid
        return new_grid
    
# Objective function
def calculate_objective(items, grid_height):
    total_score = 0
    K = 10  # Large penalty for unplaced items
    w1 = 7  # Weight for importance
    w2 = 3  # Weight for tolerance
    Y_max = grid_height - 1  # Maximum y-coordinate (0-based indexing)

    for item in items:
        if item.placed:
            y_i = item.position[1]  # y-coordinate of item
            importance_score = item.importance * (y_i / Y_max)
            tolerance_score = item.tolerance * (1 - (y_i / Y_max))
            total_score += w1 * importance_score + w2 * tolerance_score
        else:
            # Penalty for unplaced items, higher for more important items
            total_score -= K * item.importance
    return total_score

# Recursive function to explore all possible placements
def explore_placements(items, grid, index, best_arrangement):
    if index == len(items):
        # Base case: all items have been processed
        current_score = calculate_objective(items, grid.height)
        if current_score > best_arrangement['score']:
            # Update best arrangement
            best_arrangement['score'] = current_score
            best_arrangement['grid'] = grid.copy()
            best_arrangement['items'] = copy.deepcopy(items)
        return

    item = items[index]
    # Try both orientations: 0 and 90 degrees
    for rotation in [0, 90]:
        item.rotation = rotation
        # Try all positions on grid
        for y in range(grid.height):
            for x in range(grid.width):
                if grid.can_place(item, x, y):
                    # Place item
                    grid.place_item(item, x, y)
                    item.placed = True
                    item.position = (x, y)
                    # Recurse to next item
                    explore_placements(items, grid, index + 1, best_arrangement)
                    # Backtrack
                    grid.remove_item(item, x, y)
                    item.placed = False
                    item.position = None
    # Option to not place the item
    item.placed = False
    item.position = None
    explore_placements(items, grid, index + 1, best_arrangement)

def main():
    fridge_width = 10   # Number of columns (x-axis)
    fridge_height = 10  # Number of rows (y-axis)
    # TODO: Apply heuristics for performance; infeasible execution time for dimensions 12x12 and above

    # Create Grid representing fridge space
    grid = Grid(fridge_width, fridge_height)

    # Define the items
    items = items_1

    # Define object to track details of best arrangement
    best_arrangement = {
        'score': float('-inf'),
        'grid': None,
        'items': None
    }

    # Start exploring placements
    explore_placements(items, grid, 0, best_arrangement)

    # Output the best arrangement
    print(f"Best Objective Score: {best_arrangement['score']}")
    print("Best Item Placements:")
    for item in best_arrangement['items']:
        if item.placed:
            print(f"Item '{item.name}' placed at {item.position} with rotation {item.rotation} degrees.")
        else:
            print(f"Item '{item.name}' was not placed.")
    print("Grid Layout:")
    for row in best_arrangement['grid'].cells:
        print(' '.join([str(cell) if cell is not None else '.' for cell in row]))
    # Visualize
    visualize(best_arrangement)


if __name__ == "__main__":
    start_time = time.time() # Execution time
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
