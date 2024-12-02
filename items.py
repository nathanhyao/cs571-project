# items.py
# This file contains predefined items with their metadata such as dimensions, temperature tolerance, and importance.

class Item:
    def __init__(self, item_id, name, height, width, importance, tolerance, color='black'):
        self.item_id = item_id
        self.name = name
        self.height = height    # Use inches for reference, for height and width
        self.width = width
        self.importance = importance
        self.tolerance = tolerance
        self.area = self.height * self.width
        self.placed = False
        self.position = None    # (x, y)
        self.rotation = 0       # 0 or 90 degrees
        self.color = color      # You can choose colors at https://htmlcolorcodes.com/

    def rotated_dimensions(self):
        if self.rotation == 0:
            return self.width, self.height
        else:
            return self.height, self.width

    def __str__(self):
        return (f"{self.item_id}. {self.name} (Size: {self.height}x{self.width}, "
                f"Importance: {self.importance}, Tolerance: {self.tolerance})")

# Predefined list of items
predefined_items = [

    # High importance, low tolerance
    Item(1, "Milk", 4, 4, 10, 2, '#f3f3f3'), # Small
    Item(2, "Beef", 7, 4, 7, 2, '#c8653c'), # Medium
    Item(3, "Lettuce", 8, 8, 8, 3, '#7ed347'), # Large
    Item(4, "Eggs", 12, 4, 10, 3, '#2fb1d8'),

    # High importance, high tolerance
    Item(5, "Ketchup", 4, 2, 8, 9, '#f03030'), # Small
    Item(6, "Pickles", 4, 4, 6, 8, '#2b892a'), # Medium
    Item(7, "Beers", 12, 6, 9, 10, '#c78982'), # Large
    
    # Low importance, low tolerance
    Item(8, "Butter", 4, 1, 4, 4, '#f5efd7'),
    Item(9, "Cheese", 6, 4, 3, 3, '#efb350'),
    Item(10, "Carrots", 12, 6, 3, 4, '#f57c30'),

    # Low importance, high tolerance
    Item(11, "Hot Sauce", 2, 2, 5, 10, '#c82831'),
    Item(12, "Water", 3, 3, 4, 10, '#c7e0f0'),
    Item(13, "Sodas", 6, 4, 3, 10, '#f6e8a2'),

    # Misc.
    Item(14, "Cucumber", 8, 2, 5, 4, '#4ab956'),
    Item(15, "Steak", 10, 8, 6, 2, '#ee917d'),
    Item(16, "Chicken", 12, 9, 5, 2, '#e9c584'),
    Item(17, "Apple", 3, 3, 1, 10, '#f03030'),
]

# Select items based on their ID
item_set_1 = {2,4,6,8,10,12}
item_set_2 = {1,2,3,4,5,6,7,8,9,10}
item_set_3 = {1,3,5,7,9,11,13,15,17,2}

# For testing, choose item set by changing item_set_x to desired variable
selected_items = list(filter(lambda item: item.item_id in item_set_1, predefined_items))

test_details = {
    'items': selected_items,
    'fridge_width': 10,
    'fridge_height': 10,
}