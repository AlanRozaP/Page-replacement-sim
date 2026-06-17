import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from algorithms.optimal import Optimal

def test_optimal_basic():
    refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    opt = Optimal(frames=3, reference_string=refs)
    faults = 0
    for page in refs:
        if not opt.access(page):
            faults += 1
    assert faults == 7

def test_optimal_evicts_farthest():
    refs = [1, 2, 3, 1, 4]
    opt = Optimal(frames=3, reference_string=refs)
    for page in refs:
        opt.access(page)
    assert opt.page_faults == 4
