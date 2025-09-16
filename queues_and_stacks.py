def sep():
    print("".center(55, "="))

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print(f"The {element} added successfully.")

    def pop(self):
        if self.isEmpty():
            print("Empty list!")
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Empty list!")
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0
    
    def length(self):
        return len(self.stack)


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
        print(f"The {element} added successfully.")

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty!")
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            print("The queue is empty!")
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0
    
stack = Stack()
queue = Queue()
while True:

    sep(); print("Enter [1] Stack [2] Queue [3] Exit")

    sep(); discion = input("Enter what you want: ").strip()

    if discion == "1":
        while True:
            sep()
            print("Enter [1] for adding [2] Removing [3] Last element [4] Size [5] Exit")
            choice = input("Enter what you want: ").strip()
            sep()
            if choice == "1":
                stack_in = input("Enter what you want: ").strip()
                stack.push(stack_in)
                print(f"Stack = {stack.stack}")
                
            
            elif choice == "2":
                popped = stack.pop()
                print(f"Pop = {popped}")
                
            
            elif choice == "3":
                top = stack.peek()
                print(f"Peek = {top}")
                

            elif choice == "4":
                print(stack.length())
                print(f"Size of stack = {stack.length()}")

            elif choice == "5":
                print("Bye Bye\nExiting...")
                break

            else:
                print("Invalid choice!")
                
            

    elif discion == "2":
        while True:
            sep(); print("Enter [1] for adding [2] Removing [3] First element [4] Size [5] Exit")
            sep(); choice = input("Enter what you want: ").strip()
            sep()
            if choice == "1":
                queue_in = input("Enter what you want: ").strip()
                queue.enqueue(queue_in)
                print(f"Enqueue = {queue.queue}")
                
            
            elif choice == "2":
                dequeued = queue.dequeue()
                print(f"Dequeue = {dequeued}")
                

            elif choice == "3":
                first = queue.peek()
                print(f"Peek = {first}")
                

            elif choice == "4":
                queue.size()
                print(f"Size of queue = {queue.size()}")
                

            elif choice == "5":
                print("Bye Bye\nExiting...")
                break

            else:
                print("Invalid choice.")


        # sep()
    elif discion == "3":
        print("Bye Bye\n Exiting...")
        break

    else:
        sep()
        print("Please choose [1] , [2] or [3]")
        continue

