from queue import LifoQueue

class MyQueue:   # <-- class name must match LeetCode expectation
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()

    def push(self, data: int) -> None:
        # Step 1: Move all elements from input â output
        while not self.input.empty():
            self.output.put(self.input.get())

        # Step 2: Push new element into input
        self.input.put(data)

        # Step 3: Move everything back from output â input
        while not self.output.empty():
            self.input.put(self.output.get())

    def pop(self) -> int:
        if self.input.qsize() == 0:
            raise IndexError("Queue is empty")
        return self.input.get()

    def peek(self) -> int:
        if self.input.qsize() == 0:
            raise IndexError("Queue is empty")
        # The "front" of queue is at the top of input stack
        return self.input.queue[-1]

    def empty(self) -> bool:
        return self.input.qsize() == 0

