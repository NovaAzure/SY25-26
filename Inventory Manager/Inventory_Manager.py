# Initialize the inventory dictionary
inventory = {}

# Main program loop
while True:
    print("\nOptions:")
    print("[1] Add")
    print("[2] Remove")
    print("[3] List")
    print("[4] Exit")
    choice = input("Select an option (1-4): ").strip() # Get user choice and strip whitespace

    if choice == "1":
        name = input("Enter item name: ").strip().capitalize() # Get item name, strip whitespace and capitalize
        try:
            qty = int(input(f"How many {name}s? ").strip()) # Get quantity, strip whitespace
            # Add or update the item quantity in the inventory
            inventory[name] = inventory.get(name, 0) + qty
            print(f"Added {qty} {name}(s) to inventory.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    elif choice == "2":
        name = input("Which item would you like to remove? ").strip().capitalize()
        if name in inventory:
            del inventory[name]
            print(f"Removed {name} from inventory.")
        else:
            print(f"{name} not found in inventory.")

    elif choice == "3":
        if inventory:
            print("\nCurrent Inventory:")
            for item, qty in inventory.items():
                print(f"- {item}: {qty}")
        else:
            print("Inventory is empty.")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break # Exit the while loop

    else:
        print("Invalid choice. Please select an option from 1 to 4.")