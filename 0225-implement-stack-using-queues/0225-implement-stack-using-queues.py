from queue import Queue

class MyStack:

    def __init__(self):
        self.q = Queue()
        
    def push(self, x: int) -> None:
        # Store current size
        s = self.q.qsize()
        # Add new element
        self.q.put(x)
        # Move all previous elements behind the new one
        for _ in range(s):
            self.q.put(self.q.get())
        
    def pop(self) -> int:
        # Removes the front element (stack's top)
        return self.q.get()
        
    def top(self) -> int:
        # Access the first element in the queue (stack's top)
        return self.q.queue[0]
        
    def empty(self) -> bool:
        # Return True if empty, else False
        return self.q.qsize() == 0
