from Event_management import  UserInterface

ui = UserInterface()

while True:
    print("\nMenu:")
    print("1. Search Event")
    print("2. Add Event")
    print("3. Delete Event")

    print("0. Exit")

    choice = input("\nEnter your choice: ")
   
    if choice == "1":
        ui.search_event()
    elif choice == "2":
        ui.add_event()
    elif choice == "3":
        ui.delete_event()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")