from algorithms.base import PageReplacementAlgorithm

class LRU(PageReplacementAlgorithm):
    def __init__(self, frames: int):
        super().__init__(frames)
        self.memory = []
        self.memory_set = set()

    def access(self, page: int) -> bool:
        if page in self.memory_set:
            self.hits += 1
            self.memory.remove(page)
            self.memory.append(page)
            return True
        self.page_faults += 1
        if len(self.memory) < self.frames:
            self.memory.append(page)
            self.memory_set.add(page)
        else:
            evicted = self.memory.pop(0)
            self.memory_set.remove(evicted)
            self.memory.append(page)
            self.memory_set.add(page)
        return False
