task = input("Enter your task: ")

valid_priorities = ["high", "medium", "low"]

while True:
    priority = input("Priority (high/medium/low): ").lower()
    
    if priority in valid_priorities:
        break
    else:
        print("Please enter a valid priority (high/medium/low).")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")


match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority level"
        
if time_bound == "yes":
    reminder += " that require immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time"
    
    
print("\n" + reminder)