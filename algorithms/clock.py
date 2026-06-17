from algorithms.base import PageReplacementAlgorithm

class Clock(PageReplacementAlgorithm):
    def __init__(self, frames: int):
        super().__init__(frames)
        self.memory = []
        self.reference_bits = []
        self.memory_set = set()
        self.hand = 0

    def access(self, page: int) -> bool:
        if page in self.memory_set:
            self.hits += 1
            idx = self.memory.index(page)
            self.reference_bits[idx] = 1
            return True
        self.page_faults += 1
        if len(self.memory) < self.frames:
            self.memory.append(page)
            self.reference_bits.append(0)
            self.memory_set.add(page)
        else:
            while True:
                if self.reference_bits[self.hand] == 0:
                    evicted = self.memory[self.hand]
                    self.memory_set.remove(evicted)
                    self.memory[self.hand] = page
                    self.reference_bits[self.hand] = 1
                    self.memory_set.add(page)
                    self.hand = (self.hand + 1) % self.frames
                    break
                else:
                    self.reference_bits[self.hand] = 0
                    self.hand = (self.hand + 1) % self.frames
        return False
