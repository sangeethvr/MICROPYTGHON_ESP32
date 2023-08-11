import time
import _thread as thread  # For MicroPython v1.14 and earlier, use "import _thread" instead

# Task functions
def task1():
    while True:
        print("Task 1 is running")
        time.sleep(1)

def task2():
    while True:
        print("Task 2 is running")
        time.sleep(2)

# Create and start threads
thread.start_new_thread(task1, ())
thread.start_new_thread(task2, ())

# Main loop
while True:
    pass  # The main loop doesn't need to do anything in this example
