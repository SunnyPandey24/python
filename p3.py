# Simple To-Do List in Python

tasks = []

def show_tasks():
    if not tasks:
        print("✅ No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully ✅")
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        show_tasks()
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed successfully ❌")
        except (IndexError, ValueError):
            print("Invalid task number.")
    elif choice == '4':
        print("Exiting To-Do List. Goodbye 👋")
        break
    else:
        print("Invalid choice! Try again.")
