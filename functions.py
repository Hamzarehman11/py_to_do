import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load existing tasks from the JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return [] 
    return []


def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description, due_date):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,  # Auto-incrementing ID
        "task_no": len(tasks) + 1,  # Same as ID for now
        "description": description.strip(),
        "due_date": due_date.strip(),
        "status": "pending"  # Default status
    }
    tasks.append(task)
    save_tasks(tasks) 
    print(f"Task '{description}' added successfully!")


def update_task(task_id, desc=None, due_date=None):
    print('desc, due_date>>>>>>>>', desc, due_date)
    tasks = load_tasks()
    item = next((task for task in tasks if task["id"] == int(task_id)), None)
    if item == None:
        print('Item with id ' + task_id + ' does not exist')
    else:
     updated_task = {
        **item,  # Spread old properties
        "description": desc.strip() if desc else item["description"],
        "due_date": due_date.strip() if due_date else item["due_date"],
    }
     print('updated_task>>>>>>>>', updated_task)
     tasks = [updated_task if task["id"] == int(task_id) else task for task in tasks]
     save_tasks(tasks) 
    print('Update Existing task prompt')

def get_task():
    tasks = load_tasks()
    if len(tasks) == 0:
        print('No tasks to show. Add some new tasks')
    else:
     for task in tasks:
        print('\n', task)


def delete_task(task_id):
    tasks = load_tasks()
    item = next((task for task in tasks if task["id"] == int(task_id)), None)
    if item == None:
        print('Item with id ' + task_id + ' does not exist')
    else:
     tasks.remove(item)
     save_tasks(tasks) 
    print('tasks>>>>',tasks)
