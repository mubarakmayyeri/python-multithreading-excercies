import threading
import time


done = False

# Target functions
def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)

            
def display():
    counter = 0
    while True:
        time.sleep(1)
        counter += 2
        print(counter)
      
# Passing the target function to thread
# threading.Thread(target=worker).start()

# Daemon threading
threading.Thread(target=display, daemon=True).start()

# Getting an input from User
input("Press 'Enter' to quit the process...\n")

done = True