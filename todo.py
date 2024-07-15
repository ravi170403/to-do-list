import os
import json
from datetime import datetime

TODO_FILE = 'todos.json'

# Load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

def add_task(description, priority, due_date):
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task removed: {removed['description']}")
    else:
        print("Invalid task index")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print(f"Task marked as completed: {tasks[index]['description']}")
    else:
        print("Invalid task index")

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i}. {task['description']} | Priority: {task['priority']} | Due: {task['due_date']} | Status: {status}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Task Description: ")
            priority = input("Priority (high, medium, low): ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            add_task(description, priority, due_date)
        elif choice == '2':
            index = int(input("Task index to remove: "))
            remove_task(index)
        elif choice == '3':
            index = int(input("Task index to complete: "))
            complete_task(index)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
