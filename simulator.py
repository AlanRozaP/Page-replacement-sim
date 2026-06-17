from typing import List, Dict, Any
from algorithms.fifo import FIFO
from algorithms.lru import LRU
from algorithms.optimal import Optimal
from algorithms.clock import Clock

class Simulator:
    def __init__(self, frames: int, reference_string: List[int]):
        self.frames = frames
        self.reference_string = reference_string

    def run_all(self) -> Dict[str, Dict[str, Any]]:
        algorithms = {
            "FIFO": FIFO(self.frames),
            "LRU": LRU(self.frames),
            "Optimal": Optimal(self.frames, self.reference_string),
            "Clock": Clock(self.frames),
        }
        results = {}
        for name, algo in algorithms.items():
            for page in self.reference_string:
                algo.access(page)
            results[name] = {
                "faults": algo.page_faults,
                "hits": algo.hits,
                "hit_rate": algo.hit_rate(),
            }
        return results

    @staticmethod
    def format_results(results: Dict[str, Dict[str, Any]], title: str = "Results") -> str:
        lines = []
        lines.append(f"\n{'='*50}")
        lines.append(f"  {title}")
        lines.append(f"{'='*50}")
        lines.append(f"{'Algorithm':<12} {'Faults':>8} {'Hits':>8} {'Hit Rate':>10}")
        lines.append("-" * 50)
        for name, data in results.items():
            lines.append(f"{name:<12} {data['faults']:>8} {data['hits']:>8} {data['hit_rate']:>9.2%}")
        lines.append("=" * 50)
        return "\n".join(lines)
