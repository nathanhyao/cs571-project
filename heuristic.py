import copy

K = 100  # Large penalty for unplaced items
w1 = 7  # Weight for importance
w2 = 3  # Weight for tolerance

def estimate_remaining_score(items, index, grid_height):
    estimated_score = 0
    for i in range(index, len(items)):
        item = items[i]
        # Assume item can be placed at the best position
        max_importance_score = item.importance
        max_tolerance_score = item.tolerance
        estimated_score += w1 * max_importance_score + w2 * max_tolerance_score
    return estimated_score

# Modified explore_placements function with heuristic pruning
def explore_placements(items, grid, index, best_arrangement, current_score):
    if index == len(items):
        # Base case: all items have been processed
        if current_score > best_arrangement['score']:
            best_arrangement['score'] = current_score
            best_arrangement['grid'] = grid.copy()
            best_arrangement['items'] = copy.deepcopy(items)
        return

    item = items[index]
    item_placed = False
    # Try both orientations: 0 and 90 degrees
    for rotation in [0, 90]:
        item.rotation = rotation
        item_width, item_height = item.rotated_dimensions()
        # Traverse grid positions from front to back (higher y to lower y)
        for y in range(grid.height - item_height, -1, -1):
            for x in range(grid.width - item_width + 1):
                if grid.can_place(item, x, y):
                    # Place item
                    grid.place_item(item, x, y)
                    item.placed = True
                    item.position = (x, y)
                    # Calculate incremental score
                    importance_score = item.importance * ((y + item_height - 1) / (grid.height - 1))
                    tolerance_score = item.tolerance * (1 - (y / (grid.height - 1)))
                    delta_score = w1 * importance_score + w2 * tolerance_score
                    new_score = current_score + delta_score
                    # Estimate upper bound
                    remaining_score = estimate_remaining_score(items, index + 1, grid.height)
                    upper_bound = new_score + remaining_score
                    if upper_bound > best_arrangement['score']:
                        # Continue searching
                        explore_placements(items, grid, index + 1, best_arrangement, new_score)
                    grid.remove_item(item, x, y)
                    item.placed = False
                    item.position = None
                    item_placed = True
            if item_placed:
                break
        if item_placed:
            break

    penalty = -K * item.importance
    new_score = current_score + penalty
    # Estimate upper bound
    remaining_score = estimate_remaining_score(items, index + 1, grid.height)
    upper_bound = new_score + remaining_score
    if upper_bound > best_arrangement['score']:
        explore_placements(items, grid, index + 1, best_arrangement, new_score)