# use the different queue options
# https://www.geeksforgeeks.org/queue-in-python/

# using dqueue
from collections import deque


def dequeue():
    # Initialize a queue
    q = deque()

    # Adding elements to a queue
    q.append('a')
    q.append('b')
    q.append('c')

    print("initial queue")
    print(q)

    # removing elements from the queue
    print("\n2 Elements dequeued")
    node = q.popleft()
    print(q.popleft())
    # print(q.popleft())

    print("queue after removing elements")
    print(q)

    print("append two elements on left")
    q.appendleft('z')
    q.appendleft('y')
    print(q)

    print("append two elements on right")
    q.append('d')
    q.append('e')
    print(q)

    return

dequeue()

