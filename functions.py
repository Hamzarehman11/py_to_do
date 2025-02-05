import json
import os
from datetime import datetime

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
    
    try:
        # Validate if the due_date matches the correct format
        formatted_date = datetime.strptime(due_date, "%d-%m-%Y")     
        print('formatted_date>>>>',formatted_date)   
        # If parsing is successful, add the task
        task = {
            "id": len(tasks) + 1,
            "task_no": len(tasks) + 1,
            "description": description.strip(),
            "due_date": formatted_date.strftime("%d-%m-%Y"),
            "status": "pending"
        }
        tasks.append(task)
        save_tasks(tasks) 
        print(f"✅ Task '{description}' added successfully!")
        return True

    except ValueError:
        print("❌ Error: Incorrect date format! Please enter the date in DD-MM-YYYY format.")
        return False


def update_task(task_id, desc=None, due_date=None):
    tasks = load_tasks()
    item = next((task for task in tasks if task["id"] == int(task_id)), None)
    if item == None:
        print('Item with id ' + task_id + ' does not exist')
    else:
     updated_task = {
        **item,
        "description": desc.strip() if desc else item["description"],
        "due_date": due_date.strip() if due_date else item["due_date"],
    }
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
