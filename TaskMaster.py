import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                idx = int(input("Delete which number? ")) - 1
                tasks.pop(idx)
                save_tasks(tasks)
            except:
                print("Invalid input.")
        elif choice == "4":
            break

main()
