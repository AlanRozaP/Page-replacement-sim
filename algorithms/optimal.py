from algorithms.base import PageReplacementAlgorithm

class Optimal(PageReplacementAlgorithm):
    def __init__(self, frames: int, reference_string: list):
        super().__init__(frames)
        self.reference_string = reference_string
        self.current_index = 0
        self.memory = []
        self.memory_set = set()

    def access(self, page: int) -> bool:
        if page in self.memory_set:
            self.hits += 1
            self.current_index += 1
            return True
        self.page_faults += 1
        if len(self.memory) < self.frames:
            self.memory.append(page)
            self.memory_set.add(page)
        else:
            farthest = -1
            evict_idx = 0
            for i, mem_page in enumerate(self.memory):
                try:
                    next_use = self.reference_string.index(mem_page, self.current_index + 1)
                except ValueError:
                    next_use = float('inf')
                if next_use > farthest:
                    farthest = next_use
                    evict_idx = i
            evicted = self.memory.pop(evict_idx)
            self.memory_set.remove(evicted)
            self.memory.append(page)
            self.memory_set.add(page)
        self.current_index += 1
        return False
