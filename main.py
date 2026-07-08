import json
FILE_NAME = "tasks.json"
# Load tasks from file
try:
    with open(FILE_NAME, "r") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []


# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")
        save_tasks()
        
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                          
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    save_tasks()
                    print(f"Task '{deleted_task}' deleted successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")
                
    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break
    
    else:
        print("Invalid choice! Please try again.")