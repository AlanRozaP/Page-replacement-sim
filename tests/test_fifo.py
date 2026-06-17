import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from algorithms.fifo import FIFO

def test_fifo_basic():
    fifo = FIFO(frames=3)
    refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    faults = 0
    for page in refs:
        if not fifo.access(page):
            faults += 1
    assert faults == 9
