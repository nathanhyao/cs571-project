def greedy_placement(items, grid):
    for item in items:
        placed = False
        # Try both orientations: 0 and 90 degrees
        for rotation in [0, 90]:
            item.rotation = rotation
            item_width, item_height = item.rotated_dimensions()
            for y in range(grid.height - item_height, -1, -1):
                for x in range(grid.width - item_width + 1):
                    if grid.can_place(item, x, y):
                        # Place item
                        grid.place_item(item, x, y)
                        item.placed = True
                        item.position = (x, y)
                        placed = True
                        break
                if placed:
                    break
            if placed:
                break
        if not placed:
            item.placed = False
            item.position = None