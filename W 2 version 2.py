# 2. Simple To-Do List Something that helps you keep track of everything and pending tasks. You can create a simple to-do list program where users can add, remove, and view tasks. If you’re new to creating lists then this is a cool simple project to work on.



tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter the task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added.")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("Select a task number to remove:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number: "))
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed.")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
