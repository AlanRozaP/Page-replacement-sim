from collections import deque
from algorithms.base import PageReplacementAlgorithm

class FIFO(PageReplacementAlgorithm):
    def __init__(self, frames: int):
        super().__init__(frames)
        self.memory = deque()
        self.memory_set = set()

    def access(self, page: int) -> bool:
        if page in self.memory_set:
            self.hits += 1
            return True
        self.page_faults += 1
        if len(self.memory) < self.frames:
            self.memory.append(page)
            self.memory_set.add(page)
        else:
            evicted = self.memory.popleft()
            self.memory_set.remove(evicted)
            self.memory.append(page)
            self.memory_set.add(page)
        return False
