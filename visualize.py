import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import to_rgba

def visualize(arrangement, alg_type="Algorithm"):
    grid = arrangement['grid']
    items = arrangement['items']

    # Helper: create mapping from item id to its color, and to name
    id_to_color = {}
    id_to_name = {}
    for i in items:
        id_to_color[i.item_id] = i.color
        id_to_name[i.item_id] = i.name

    # Create color matrix corresponding to the grid
    color_grid = []
    for row in grid.cells:
        color_row = []
        for cell in row:
            if cell is None:
                # Represent empty space with lightgrey
                color_row.append('lightgrey')
            else:
                # Set cell to designated color, else set to 'black'
                color_row.append(id_to_color.get(cell, 'black'))
        color_grid.append(color_row)
    
    # Convert 'color_grid' to RGBA values
    rgba_grid = []
    for row in color_grid:
        rgba_row = [to_rgba(color) for color in row]
        rgba_grid.append(rgba_row)
    
    # Display color matrix; use blank colormap since colors are already defined
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(rgba_grid, aspect='equal')

    # Remove axis ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Add grid lines for better readability
    num_rows = len(grid.cells)
    num_cols = len(grid.cells[0]) if num_rows > 0 else 0
    for i in range(num_rows + 1):
        ax.axhline(i - 0.5, color='black', linewidth=0.5)
    for j in range(num_cols + 1):
        ax.axvline(j - 0.5, color='black', linewidth=0.5)

    # Loop through each cell in the matrix to add text annotations
    for i in range(num_rows):
        for j in range(num_cols):
            cell = grid.cells[i][j]
            if cell is not None:
                # Retrieve the item's name; fallback to ID if name not found
                text = id_to_name.get(cell, str(cell))
                # Add text annotation to the center of the cell
                ax.text(j, i, text, ha='center', va='center', color='black', fontsize=5)

    # Set title
    ax.set_title(f'{alg_type}: Best Arrangement Found, {num_cols}x{num_rows} Grid', fontsize=12)

    # Create legend handles
    legend_handles = []
    for i in items:
        # Include information abt each item in the legend
        patch = mpatches.Patch(
            color=id_to_color[i.item_id], 
            label=f"id {i.item_id}: {i.name}, " +
            f"{i.width}x{i.height}, I={i.importance}, T={i.tolerance}"
            )
        legend_handles.append(patch)
    # Add legend to the plot
    # ax.legend(handles=legend_handles, bbox_to_anchor=(1.05, 1), loc='best', borderaxespad=0.0)
    ax.legend(handles=legend_handles, bbox_to_anchor=(1.05, 1), loc='best', borderaxespad=0.0)

    # Adjust layout to make room for the legend
    plt.tight_layout()

    # Display the plot
    plt.show()
