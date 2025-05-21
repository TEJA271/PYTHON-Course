# 2. Simple To-Do List Something that helps you keep track of everything and pending tasks. You can create a simple to-do list program where users can add, remove, and view tasks. If you’re new to creating lists then this is a cool simple project to work on.





tasks = []


for i in range(3):
    task = input(f"Enter task {i+1}: ")
    tasks.append(task)


print("\nYour To-Do List:")
for task in tasks:
    print(f"- {task}")
