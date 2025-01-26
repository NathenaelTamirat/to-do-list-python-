# Simple To-Do List App
# show list custom made function 
def show_list(t):
    if not t:
        print("Your to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for i, task in enumerate(t, 1):
            print(f"{i}. {task}")

def add_task(t):
    task = input("What do you need to do? ")
    t.append(task)
    print(f"Task '{task}' added!")

def remove_task(t):
    show_list(t)
    idx = input("\nWhich task number would you like to remove? ")
    if idx.isdigit() and 1 <= int(idx) <= len(t):
        removed = t.pop(int(idx) - 1)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = []
    while True:
        print("\n1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            show_list(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number between 1 and 4.")

if __name__ == "__main__":
    main()
