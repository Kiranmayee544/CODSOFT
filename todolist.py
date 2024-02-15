def display_tasks(tasks):
    print("Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully!")

def remove_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task index!")

def clear_tasks(tasks):
    tasks.clear()
    print("All tasks cleared!")

def main():
    tasks = []

    while True:
        print("\n1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Clear all tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            clear_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
