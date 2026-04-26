from collections import deque

queue = deque()

def enqueue(item):
    queue.append(item)

def safe_dequeue():
    if len(queue) == 0:
        print("Queue is empty, cannot dequeue.")
        return None
    return queue.popleft()

# Example
enqueue(1)
enqueue(2)
print(safe_dequeue())
print(safe_dequeue())
print(safe_dequeue())
