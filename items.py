# items.py
# This file contains predefined items with their metadata such as dimensions, temperature tolerance, and importance.

class Item:
    def __init__(self, item_id, name, length, width, temperature_tolerance, importance):
        self.item_id = item_id
        self.name = name
        self.length = length
        self.width = width
        self.temperature_tolerance = temperature_tolerance  # in Fahrenheit
        self.importance = importance  # Score from 1 to 10

    def __str__(self):
        return (f"{self.item_id}. {self.name} (Size: {self.length}x{self.width}, "
                f"Temperature Tolerance: {self.temperature_tolerance}°F, Importance: {self.importance})")

# Predefined list of items
predefined_items = [
    Item(1, "Milk", 10, 10, 40, 8),
    Item(2, "Eggs", 5, 5, 45, 7),
    Item(3, "Butter", 3, 3, 50, 6),
    Item(4, "Cheese", 4, 4, 45, 7),
    Item(5, "Vegetables", 15, 10, 50, 9),
    Item(6, "Fruits", 12, 8, 55, 9),
    Item(7, "Juice", 8, 8, 50, 8),
    Item(8, "Meat", 10, 15, 35, 6),
    Item(9, "Fish", 8, 12, 35, 5),
    Item(10, "Yogurt", 6, 6, 40, 7),
]
