def greedy_placement(items, grid):
    for item in items:
        placed = False
        # Try both orientations: 0 and 90 degrees
        for rotation in [0, 90]:
            item.rotation = rotation
            item_width, item_height = item.rotated_dimensions()
            # Traverse grid positions from front to back (higher y to lower y)
            for y in range(grid.height - item_height, -1, -1):  # Start from front
                for x in range(grid.width - item_width + 1):
                    if grid.can_place(item, x, y):
                        # Place item
                        grid.place_item(item, x, y)
                        item.placed = True
                        item.position = (x, y)
                        placed = True
                        break  # Exit x loop
                if placed:
                    break  # Exit y loop
            if placed:
                break  # Exit rotation loop
        if not placed:
            # Item could not be placed
            item.placed = False
            item.position = None