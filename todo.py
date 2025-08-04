def show_menu():
    print("\n📋 TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

tasks = []

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ Task added: {task}")

    elif choice == '3':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            index = int(input("Enter task number to remove: "))
            removed = tasks.pop(index - 1)
            print(f"🗑 Removed task: {removed}")
        except:
            print("❌ Invalid number!")

    elif choice == '4':
        print("Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Please try again.")
