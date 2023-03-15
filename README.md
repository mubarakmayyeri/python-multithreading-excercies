# Python Multithreading Exercises
Learning multithreading in Python programming language.

## Sample Program for Multithreading
```python
import threading

def my_function():
    # code to be executed in the thread
    print("Thread started")
    # do some processing
    print("Thread finished")

# create a new thread
t = threading.Thread(target=my_function)

# start the thread
t.start()

# wait for the thread to finish
t.join()

print("Main thread finished")

```

## Resources
* NeuralNine - https://www.youtube.com/watch?v=A_Z1lgZLSNc
