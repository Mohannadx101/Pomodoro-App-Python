import time
import datetime

# Pomodoro settings
work_duration = 40 * 60  # 40 minutes in seconds
short_break_duration = 5 * 60  # 5 minutes in seconds
long_break_duration = 15 * 60  # 15 minutes in seconds
pomodoro_cycles = 4  # Number of pomodoros before a long break

# Track overall time spent
overall_time_spent = 0

def pomodoro():
    global overall_time_spent

    for i in range(pomodoro_cycles):
        print(f"\nPomodoro {i+1} ")
        work_timer(work_duration)
        overall_time_spent += work_duration

        # Print overall time spent after each short break
        print(f"\nOverall time spent so far: {datetime.timedelta(seconds=overall_time_spent)}")

        print("\nShort break ☕")
        break_timer(short_break_duration)
        overall_time_spent += short_break_duration

    print("\nLong break ️")
    break_timer(long_break_duration)
    overall_time_spent += long_break_duration

    print(f"\nOverall time spent: {datetime.timedelta(seconds=overall_time_spent)}")

def work_timer(duration):
    for i in range(duration, 0, -1):
        print(f"Time remaining: {datetime.timedelta(seconds=i)}", end="\r")
        time.sleep(1)

def break_timer(duration):
    for i in range(duration, 0, -1):
        print(f"Break time remaining: {datetime.timedelta(seconds=i)}", end="\r")
        time.sleep(1)

if __name__ == "__main__":
    pomodoro()
