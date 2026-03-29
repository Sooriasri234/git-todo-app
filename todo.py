tasks = []

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
def add_task(task):
    tasks.append(task)

if __name__ == "__main__":
    tasks.append("Learn Git")
    show_tasks()