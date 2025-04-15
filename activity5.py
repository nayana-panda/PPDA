def list_operations():
    my_list = []

    while True:
        print("\nList Operations:")
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Find an element")
        print("4. Sort the list")
        print("5. Reverse the list")
        print("6. Display list")
        print("7. Exit")

        try:
          choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            element = input("Enter element to insert: ")
            my_list.append(element)
            print(f"Element '{element}' inserted.")

        elif choice == 2:
            element = input("Enter element to delete: ")
            if element in my_list:
                my_list.remove(element)
                print(f"Element '{element}' deleted.")
            else:
                print(f"Element '{element}' not found.")

        elif choice == 3:
            element = input("Enter element to find: ")
            if element in my_list:
                print(f"Element '{element}' found.")
            else:
                print(f"Element '{element}' not found.")

        elif choice == 4:
            order = input("Sort in ascending or descending order? (a/d): ").lower()
            try:
                if order == 'a':
                    my_list.sort()
                    print("List sorted in ascending order.")
                elif order == 'd':
                    my_list.sort(reverse=True)
                    print("List sorted in descending order.")
                else:
                    print("Invalid input. Use 'a' for ascending or 'd' for descending.")
            except TypeError:
                print("List contains items that cannot be compared (e.g., mix of strings and numbers).")

        elif choice == 5:
            my_list.reverse()
            print("List has been reversed.")

        elif choice == 6:
            print(f"Current list: {my_list}")

        elif choice == 7:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

# Run the function
list_operations()
