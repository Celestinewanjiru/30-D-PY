import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

# Function to view tasks
def view_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("\nNo tasks in your list.")
    else:
        print("\nNo tasks yet.")

# Function to add a task
def add_task():
    task = input("\nEnter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"\nTask '{task}' added!")
    
    # Display all tasks after adding the new one
    view_tasks()

    # Ask if user is done or wants to add another task
    done = input("\nAre you done adding tasks? (y/n): ").lower()
    if done != 'y':
        add_task()  # Recursively add more tasks

# Main function to run the app
def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-3): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 3.")

if __name__ == "__main__":
    main()
