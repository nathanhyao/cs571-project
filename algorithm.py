
import time
import copy
from visualize import visualize
from items import test_details
from itertools import permutations, product
from greedy import greedy_placement
from heuristic import explore_placements

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
        new_grid.cells = [row[:] for row in self.cells]  # Deep copy of own grid
        return new_grid
# Objective function
def calculate_objective(items, grid_height):
    total_score = 0
    K = 100  # Large penalty for unplaced items
    w1 = 7  # Weight for importance
    w2 = 3  # Weight for tolerance
    Y_max = grid_height - 1  # Maximum y-coordinate (0-based indexing)

    for item in items:
        if item.placed:
            _, item_height = item.rotated_dimensions()
            y_i = item.position[1] # y-coordinate of item

            # (y_i + item_height - 1) to consider edge of item closest to front
            importance_score = item.importance * ((y_i + item_height - 1) / Y_max)
            tolerance_score = item.tolerance * (1 - (y_i / Y_max))
            total_score += w1 * importance_score + w2 * tolerance_score
        else:
            # Penalty for unplaced items, higher for more important items
            total_score -= K * item.importance
    return total_score

# Recursive function to explore all possible placements
def exhaustive_explore_placements(items, grid, index, heuristic_arragement):
    if index == len(items):
        # Base case: all items have been processed
        current_score = calculate_objective(items, grid.height)
        if current_score > heuristic_arragement['score']:
            # Update best arrangement
            heuristic_arragement['score'] = current_score
            heuristic_arragement['grid'] = grid.copy()
            heuristic_arragement['items'] = copy.deepcopy(items)
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
                    exhaustive_explore_placements(items, grid, index + 1, heuristic_arragement)
                    # Backtrack
                    grid.remove_item(item, x, y)
                    item.placed = False
                    item.position = None
    # Option to not place the item
    item.placed = False
    item.position = None
    exhaustive_explore_placements(items, grid, index + 1, heuristic_arragement)

def main():
    fridge_width = test_details['fridge_width'] # Number of columns (x-axis)
    fridge_height = test_details['fridge_height']  # Number of rows (y-axis)

    # Create Grid representing fridge space
    grid1 = Grid(fridge_width, fridge_height)

    # Define the items
    items = test_details['items']

################################## Greedy search ##################################################
    for item in items:
        item.priority = item.importance 
        item.placed = False
        item.position = None

    # Sort items by priority
    items.sort(key=lambda x: x.priority, reverse=True)

    # Greedy algorithm
    start_time = time.time()
    greedy_placement(items, grid1)
    greedy_time = time.time() - start_time
    greedy_score = calculate_objective(items, grid1.height)

    print(f"Greedy Algorithm Time: {greedy_time} seconds")
    print(f"Greedy Algorithm Score: {greedy_score}\n")
    print("Greedy Item Placements:")
    for item in items:
        if item.placed:
            print(f"Item '{item.name}' placed at {item.position} with rotation {item.rotation} degrees.")
        else:
            print(f"Item '{item.name}' was not placed.")
    print("\nGrid Layout:")
    for row in grid1.cells:
        print(' '.join([str(cell) if cell is not None else '.' for cell in row]))
    print()

################################## Heuristic Search ##################################################
    for item in items:
        item.placed = False
        item.position = None

    heuristic_arragement = {
        'score': float('-inf'),
        'grid': None,
        'items': None
    }

    start_time = time.time()

    # Start exploring placements with heuristic
    explore_placements(items, Grid(fridge_width, fridge_height), 0, heuristic_arragement, 0)
    heuristic_time = time.time() - start_time

    print(f"Heuristic Search Time: {heuristic_time} seconds")
    print(f"Heuristic Search Score: {heuristic_arragement['score']}\n")
    print("Heuristic Item Placements:")
    for item in heuristic_arragement['items']:
        if item.placed:
            print(f"Item '{item.name}' placed at {item.position} with rotation {item.rotation} degrees.")
        else:
            print(f"Item '{item.name}' was not placed.")
    print("\nGrid Layout:")

    for row in heuristic_arragement['grid'].cells:
        print(' '.join([str(cell) if cell is not None else '.' for cell in row]))
    print()

    visualize({'grid': grid1, 'items': items}, "Greedy")  # Greedy result
    visualize(heuristic_arragement, "Branch & Bound")  # Heuristic search result

################################## Exhaustive Search ##################################################
    grid2 = Grid(fridge_width, fridge_height)

    for item in items:
        item.placed = False
        item.position = None
        
    best_arrangement = {
        'score': float('-inf'),
        'grid': None,
        'items': None
    }

    start_time = time.time()

    exhaustive_explore_placements(items, grid2, 0, best_arrangement)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(f"\nBest Objective Score: {best_arrangement['score']}\n")
    print("Best Item Placements:")
    for item in best_arrangement['items']:
        if item.placed:
            print(f"Item '{item.name}' placed at {item.position} with rotation {item.rotation} degrees.")
        else:
            print(f"Item '{item.name}' was not placed.")
    print("\nGrid Layout:")
    for row in best_arrangement['grid'].cells:
        print(' '.join([str(cell) if cell is not None else '.' for cell in row]))
    print()

    visualize(best_arrangement, "Exhaustive")

if __name__ == "__main__":
    main()
