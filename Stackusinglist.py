stack = []

def push(item):
    stack.append(item)

def safe_pop():
    if len(stack) == 0:
        print("Stack is empty, nothing to pop.")
        return None
    return stack.pop()

# Example
push(10)
push(20)
print(safe_pop())
print(safe_pop())
print(safe_pop())
