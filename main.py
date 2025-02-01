
from functions import add_task, update_task, delete_task, get_task

def success_info():
    print('Action completed sucessfully!')
    # show_menu_prompt()1

def show_menu_prompt():
    print('Press 0 to go back to menu')

def show_menu():
    """Displays the To-Do list menu"""
    print("\n📌 To-Do List App 📌")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

def main():
     show_menu()
     while True:
        choice = input('Enter the number you want to choose: ')

        if choice == '1':
            task = input('Write your task: ')
            due_date = input('Enter due date: ')
            add_task(task,due_date)
            success_info()
        elif choice == '2':
            get_task()
            success_info()
        elif choice == '3':
            delete_task()
            success_info()
        elif choice == '4':
            update_task()
            success_info()
        elif choice == '5':
            break
        elif choice.lower() == '0':  # If the user wants to see the menu again
            show_menu()
        else:
             print("Invalid choice. Please enter a number between 1 and 4.")
    
if __name__ == '__main__':
    main()