def add_birthday(calendar, name, birthday):
    calendar[name] = birthday

def find_birthday(calendar, name):
    if name in calendar:
        return calendar[name]
    else:
        return "Birthday not found."

def main():
    birthday_calendar = {}

    while True:
        print("Birthday Calendar")
        print("1. Add a birthday")
        print("2. Find a birthday")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            birthday = input("Enter the birthday (DD/MM/YYYY): ")
            add_birthday(birthday_calendar, name, birthday)
            print("Birthday added successfully!")
        elif choice == "2":
            name = input("Enter the name: ")
            birthday = find_birthday(birthday_calendar, name)
            print(f"{name}'s birthday is on {birthday}")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
