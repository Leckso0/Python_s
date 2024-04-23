
"""
Project Idea: To-Do List Manager

"""

def add_task(todo_list, task):
    # Add a task to the to-do list
    todo_list.append(task)

def complete_task(todo_list, task_index):
    # Mark a task as completed
    if 0 <= task_index < len(todo_list):
        todo_list[task_index] += " - Completed"
    else:
        print("Invalid task index.")

def view_todo_list(todo_list):
    # View the current to-do list
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")
    else:
        print("To-Do List is empty.")

def load_todo_list(filename):
    # Load a to-do list from a file
    try:
        with open(filename, 'r') as file:
            todo_list = file.readlines()
        print("To-Do list loaded successfully.")
        return [task.strip() for task in todo_list]
    except FileNotFoundError:
        print("File not found. Unable to load the to-do list.")
        return []
    except Exception as e:
        print(f"An error occurred while loading the to-do list: {e}")
        return []

def save_todo_list(todo_list, filename):
    # Save the to-do list to a file
    with open(filename, 'w') as file:
        for task in todo_list:
            file.write(task + '\n')
    print("To-Do list saved successfully.")

def delete_task(todo_list, task_index):
    # Delete a task from the to-do list
    if 0 <= task_index < len(todo_list):
        del todo_list[task_index]
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

def main():
    # Main function to control the flow of the program
    todo_list = []

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View To-Do List")
        print("4. Save To-Do List")
        print("5. Load To-Do List")
        print("6. Delete Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "2":
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            complete_task(todo_list, task_index)
        elif choice == "3":
            view_todo_list(todo_list)
        elif choice == "4":
            filename = input("Enter the filename to save the to-do list: ")
            save_todo_list(todo_list, filename)
        elif choice == "5":
            filename = input("Enter the filename to load the to-do list: ")
            todo_list = load_todo_list(filename)
        elif choice == "6":
            task_index = int(input("Enter the task index to delete: ")) - 1
            delete_task(todo_list, task_index)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
