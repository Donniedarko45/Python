USERS_FILE = "user.txt"

def load_users():
    file = open(USERS_FILE, 'r')
    users = {}
    for line in file:
        parts = line.strip().split(':')
        username = parts[0]
        password = parts[1]
        tasks = parts[2].split(',') if parts[2] else []
        users[username] = {'password': password, 'tasks': tasks}
    return users


def save_users(users):
    with open(USERS_FILE, 'w') as file:
        for username, data in users.items():
            tasks_str = ','.join(data['tasks'])
            file.write(f"{username}:{data['password']}:{tasks_str}\n")

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
    users = load_users()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]['password'] == password:
        print("Login successful.")
        return username
    else:
        print("Invalid username or password.")
        return None

def load_tasks(username):
    users = load_users()
    return users.get(username, {}).get('tasks', [])

def save_tasks(username, tasks):
    users = load_users()
    users[username]['tasks'] = tasks
    save_users(users)

def list_all_tasks(username):
    tasks = load_tasks(username)
    if tasks:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

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
i=1
while(i>0):
    main()
    i-=1