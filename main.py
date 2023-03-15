import threading
import time


done = False

# Target function
def worker():
    global done
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)
        if counter == 10:
            done = True
        
        
        
# Passing the target function to thread
threading.Thread(target=worker).start()

# Getting an input from User
input("Press 'Enter' to quit the process...\n")

done = True