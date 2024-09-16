# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")

# Validate priority input using a loop
valid_priorities = ["high", "medium", "low"]
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in valid_priorities:
        break
    else:
        print("Please enter a valid priority (high/medium/low).")

# Validate time-bound input using a loop
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")

# Process the Task Based on Priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Provide the Customized Reminder
print(f"\nReminder: {reminder}")
