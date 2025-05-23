#10. Python To-Do List

todo = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(todo, 1):
        print(f"{i}. {task}")
    
    print("\nOptions: add / delete / exit")
    choice = input("What would you like to do? ").strip().lower()

    if choice == "add":
        task = input("Enter a task: ")
        todo.append(task)
    elif choice == "delete":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(todo):
            todo.pop(num - 1)
        else:
            print("Invalid task number.")
    elif choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
