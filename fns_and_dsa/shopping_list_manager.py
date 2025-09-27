def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            new_item = input("Enter the item to add:").strip()
            shopping_list.append(new_item)
            print(f"✅ {new_item} added to your shopping list.")
        elif choice == '2':
            # Prompt for and remove an item
            item_remove = input("enter the item that you would want to remove: ")
            if  item_remove in shopping_list:
                shopping_list.remove(item_remove) 
                print(f"🗑️ {item_remove} removed from your shopping list.")
            else:
                 print(f"⚠️ The item '{item_remove}' is not in your shopping list.")
        elif choice == '3':
            # Display the shopping list
            # Display the shopping list
            if shopping_list:
                print("🛒 Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("🛒 Your shopping list is empty.")
            
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    