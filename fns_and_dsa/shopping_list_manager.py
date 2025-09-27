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
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            new_item = input("add a new item:")
            shopping_list.append(new_item)
        elif choice == '2':
            # Prompt for and remove an item
            item_remove = input("enter the item that you would want to remove: ")
            if  item_remove in shopping_list:
                shopping_list.remove(item_remove) 
            else:
                print(f"the item {item_remove} is not in your shopping list")
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    