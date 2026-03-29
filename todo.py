tasks = []

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
def add_task(task):
    tasks.append(task)
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
def update_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index] = new_task

if __name__ == "__main__":
    tasks.append("Learn Git")
    show_tasks()