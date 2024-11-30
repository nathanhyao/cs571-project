# items.py
# This file contains predefined items with their metadata such as dimensions, temperature tolerance, and importance.

class Item:
    def __init__(self, item_id, name, height, width, importance, tolerance, color='black'):
        self.item_id = item_id
        self.name = name
        self.height = height
        self.width = width
        self.importance = importance
        self.tolerance = tolerance
        self.area = self.height * self.width
        self.placed = False
        self.position = None  # (x, y)
        self.rotation = 0     # 0 or 90 degrees
        self.color = color  # Choose colors with https://htmlcolorcodes.com/

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
    Item(1, "Milk", 6, 6, 10, 2, '#f3f3f3'),
    Item(2, "Eggs", 12, 4, 10, 3, '#2fb1d8'),
    Item(3, "Butter", 6, 4, 7, 5, '#f5efd7'),
    Item(4, "Cheese", 6, 4, 9, 4, '#efb350'),
    Item(5, "Carrots", 12, 6, 7, 5, '#f57c30'),
    Item(6, "Water", 3, 3, 4, 10, '#c7e0f0'),
    Item(7, "Soda", 2, 2, 3, 10, '#f6e8a2'),
    Item(8, "Cucumber", 8, 2, 5, 4, '#4ab956'),
    Item(9, "Steak", 10, 8, 6, 2, '#ee917d'),
    Item(10, "Chicken", 12, 9, 5, 2, '#e9c584'),
    Item(11, "Hot Sauce", 2, 2, 5, 10, '#c82831'),
    Item(12, "Ketchup", 4, 4, 8, 9, '#f03030'),
]

# Select some items based on their ids
selected = {1,2,11,6,8,12}
items_1 = list(filter(lambda item: item.item_id in selected, predefined_items))