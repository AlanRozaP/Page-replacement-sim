from abc import ABC, abstractmethod

class PageReplacementAlgorithm(ABC):
    def __init__(self, frames: int):
        self.frames = frames
        self.page_faults = 0
        self.hits = 0

    @abstractmethod
    def access(self, page: int) -> bool:
        """Return True if hit, False if page fault."""
        pass

    def hit_rate(self) -> float:
        total = self.hits + self.page_faults
        return self.hits / total if total else 0.0
