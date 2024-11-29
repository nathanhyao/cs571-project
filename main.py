# main.py

from items import predefined_items

def get_fridge_dimensions():
    while True:
        try:
            length = int(input("Enter the length of the fridge (in grid units): "))
            if length <= 0:
                print("Length must be a positive integer. Please try again.")
                continue
            width = int(input("Enter the width of the fridge (in grid units): "))
            if width <= 0:
                print("Width must be a positive integer. Please try again.")
                continue
            return length, width
        except ValueError:
            print("Invalid input. Please enter integer values for dimensions.")

def display_items():
    print("\nAvailable items to add to the fridge:")
    for item in predefined_items:
        print(item)

def get_user_items():
    selected_item_ids = set()
    while True:
        input_str = input("\nSelect items to add to the fridge. Enter the item numbers separated by commas (e.g., 1,3,5) and end with 0:\n")
        inputs = [s.strip() for s in input_str.split(',')]
        try:
            for s in inputs:
                if s == '0':
                    return [item for item in predefined_items if item.item_id in selected_item_ids]
                item_id = int(s)
                if item_id == 0:
                    return [item for item in predefined_items if item.item_id in selected_item_ids]
                if item_id < 1 or item_id > len(predefined_items):
                    print(f"Item number {item_id} is out of range. Please select valid item numbers.")
                    break
                if item_id in selected_item_ids:
                    print(f"Item number {item_id} has already been selected. Please choose different items.")
                    break
                selected_item_ids.add(item_id)
            else:
                continue
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")
        continue

def main():
    print("Welcome to the 2D Fridge Simulator!")

    # Get fridge dimensions from the user
    length, width = get_fridge_dimensions()
    print(f"\nFridge dimensions: {length} x {width}")

    # Display available items
    display_items()

    # Get user's selected items
    selected_items = get_user_items()
    print("\nYou have selected the following items:")
    for item in selected_items:
        print(item)

    # Placeholder for the algorithm implementation
    # TODO: Implement the placement algorithm here

if __name__ == "__main__":
        main()
