task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a {priority} priority task"
    case "medium":
        reminder = f"'{task}' is a {priority} priority task"
    case "low":
        reminder = f"'{task}' is a {priority} priority task"
    case _:
        print("Enter a valid task!")

if time_bound == "yes":
    print(f"Reminder: {reminder} that requires immediate attention today!")
else:
    print(f"Note: {reminder}. Consider completing it when you have free time.")
