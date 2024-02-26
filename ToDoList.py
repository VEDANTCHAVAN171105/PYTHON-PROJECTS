class TodoList:
    
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(description)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            print(f"Completed task: '{self.tasks.pop(task_index)}'")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            print(f"Deleted task: '{self.tasks.pop(task_index)}'")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")


def main():
    todo_list = TodoList()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter Task Description: ")
            todo_list.add_task(description)
        elif choice == "2":
            task_index = int(input("Enter Task Index To Mark As Completed: ")) - 1
            todo_list.mark_task_completed(task_index)
        elif choice == "3":
            task_index = int(input("Enter Task Index To Delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please Try Again...")

if __name__ == "__main__":
    main()