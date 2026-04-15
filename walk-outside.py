import datetime
import os

# Configuration
LOG_FILE = "walk_log.txt"
WALK_GOAL_MINUTES = 60

def daily_reminder():
    today = str(datetime.date.today())
    
    # Check if we already logged a walk today
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            if today in f.read():
                print(f"🎉 Great job! You already finished your {WALK_GOAL_MINUTES}-minute walk today.")
                return

    print("--- 🚶 DAILY WALK REMINDER ---")
    print(f"You haven't logged your {WALK_GOAL_MINUTES}-minute walk yet.")
    status = input("Did you just finish it? (y/n): ").strip().lower()

    if status == 'y':
        with open(LOG_FILE, "a") as f:
            f.write(f"{today}: Completed 1 hour walk\n")
        print("Nice! Logging it now. See you tomorrow!")
    else:
        print("Shoes on! The fresh air is waiting for you. 🌳")

if __name__ == "__main__":
    daily_reminder()
