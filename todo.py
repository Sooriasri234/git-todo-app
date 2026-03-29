tasks = []

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    
    if __name__ == "__main__":
        while True:
            print("\n1.Add 2.Delete 3.View 4.Exit")
            choice = int(input("Enter choice: "))

            if choice == 1:
                task = input("Enter task: ")
                add_task(task)

            elif choice == 2:
                index = int(input("Enter task number: ")) - 1
                delete_task(index)

            elif choice == 3:
                show_tasks()

            elif choice == 4:
                break
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
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