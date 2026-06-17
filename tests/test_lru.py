import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from algorithms.lru import LRU

def test_lru_basic():
    lru = LRU(frames=3)
    refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    faults = 0
    for page in refs:
        if not lru.access(page):
            faults += 1
    assert faults == 10

def test_lru_recency_updates_on_hit():
    lru = LRU(frames=2)
    lru.access(1)  # fault
    lru.access(2)  # fault
    lru.access(1)  # hit — 1 is now most recent
    lru.access(3)  # fault — evicts 2 (least recent)
    assert 2 not in lru.memory_set
    assert 1 in lru.memory_set
    assert lru.page_faults == 3
