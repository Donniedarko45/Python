USERS_FILE = "user.txt"

def load_users():
    pass #file handling requirement


def save_users(users):
    pass # file handling requirements

def register():
    users = load_users()
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose another one.")
        return
    password = input("Enter a password: ")
    users[username] = {'password': password, 'tasks': []}
    save_users(users)
    print("Registration successful.")

def login():
    pass #file-handling requirements 

def load_tasks(username):
    pass #file-handling requirements

def save_tasks(username, tasks):
    pass #file-handling requirements 

def list_all_tasks(username):
     pass #file-handling requirements

def add_task(username):
    task = input("Enter a new task: ")
    tasks = load_tasks(username)
    tasks.append(task)
    save_tasks(username, tasks)
    print("Task added successfully.")
    
def update_task(username):
    tasks = load_tasks(username)
    list_all_tasks(username)
    index = int(input("Enter the task number to update: "))
    if 1 <= index <= len(tasks):
        new_task_name = input("Enter the new task name: ")
        tasks[index - 1] = new_task_name
        save_tasks(username, tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(username):
    tasks = load_tasks(username)
    list_all_tasks(username)
    index = int(input("Enter the task number to delete: "))
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
        save_tasks(username, tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    print("\nLogged in as:", username)
                    print("1. List all tasks")
                    print("2. Add a task")
                    print("3. Update a task")
                    print("4. Delete a task")
                    print("5. Logout")
                    inner_choice = input("Enter your choice: ")
                    if inner_choice == '1':
                        list_all_tasks(username)
                    elif inner_choice == '2':
                        add_task(username)
                    elif inner_choice == '3':
                        update_task(username)
                    elif inner_choice == '4':
                        delete_task(username)
                    elif inner_choice == '5':
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
