class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
from collections import deque
deque_info = deque(["giorgi", "nino", "giorgi", "nika", "ana", "nino", "ana"])
set_info = set(deque_info)
print(set_info)
print(len(set_info))