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

            
def display(input):
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(f'{input}: {counter}\n')
      
# Passing the target function to thread
# threading.Thread(target=worker).start()

# Daemon threading
threading.Thread(target=display, daemon=True, args=('First Thread', )).start()

threading.Thread(target=display, daemon=True, args=('Second Thread', )).start()

threading.Thread(target=display, daemon=True, args=('Third Thread', )).start()

# Getting an input from User
input("Press 'Enter' to quit the process...\n")

done = True